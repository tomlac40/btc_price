# btc_price

## Installation

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `nicehash`.
1. Download _all_ the files from the `custom_components/btc_price/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Add wanted currency to `configuration.yaml`
   ```
   sensor:   
     - platform: btc_price
       currency_name: "usd"
    
     - platform: btc_price
       currency_name: "eur"  
   ```
1. Restart Home Assistant
1. Sensors created:
   ```
   sensor.btc_price_usd
   sensor.btc_price_eur
   ```   

#### Available currencies
 - ARS

 - AUD
 - BRL
 - CAD
 - CHF
 - CLP
 - CNY
 - CZK
 - DKK
 - EUR
 - GBP
 - HKD
 - HRK
 - HUF
 - INR
 - ISK
 - JPY
 - KRW
 - NGN
 - NZD
 - PLN
 - RON
 - RUB
 - SEK
 - SGD
 - THB
 - TRY
 - TWD
 - USD
