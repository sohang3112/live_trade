# live_trade
Buying, Selling and Viewing Live Trade Data using Zerodha Kite

## Requirements
- Python 3
- Chrome Browser must be installed (preferably latest version).
- Pip Install:
    - kiteconnect
    - pyotp  
    - selenium
    - webdriver-manager

## Configuration
Create a file `config.ini` and fill your Zerodha account details in it
like this:

```
[zerodha]
api_key =     # API Key here
api_secret =  # API Secret here
user_id =     # User ID here
password =    # Password here
totp_key =    # TOTP Key here
```
