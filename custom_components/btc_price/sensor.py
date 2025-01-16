import voluptuous as vol
from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from blockchain import exchangerates, statistics
import logging


SCAN_INTERVAL = timedelta(minutes=5)

CONF_CURRENCY_NAME = "currency_name"

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="BTC Price"): cv.string,
    vol.Optional(CONF_CURRENCY_NAME, default="usd"): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    currency_name = config.get(CONF_CURRENCY_NAME).strip()
    
    if currency_name.upper() not in exchangerates.get_ticker():
      _LOGGER.warning("Currency %s is not available. Using USD", currency_name)
      currency_name = "usd"

    add_entities([BTCPriceSensor(name, currency_name)], True)

class BTCPriceSensor(Entity):
    def __init__(self, name, currency):
        self._name = f"{name} ({currency.upper()})"
        self._currency = currency.upper()
        self._state = None
        
        if currency == "eur":
          self._unit_of_measurement = "€"
        elif  currency == "usd":
          self._unit_of_measurement = "$"
        else:
          self._unit_of_measurement = self._currency

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state
        
    @property
    def unit_of_measurement(self):
        """Return the unit of measurement this sensor expresses itself in."""
        return self._unit_of_measurement    

    def update(self):
        self._state = exchangerates.get_ticker()[self._currency].last
