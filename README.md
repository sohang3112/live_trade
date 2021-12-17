# live_trade
Buying, Selling and Viewing Live Trade Data using Zerodha Kite

## Requirements
- Python 3, with the following Python packages installed using pip:
    - datetime 
    - kiteconnect
    - pyperclip 
    - pyotp  
    - selenium
    - tg-logger

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