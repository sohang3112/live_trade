from configparser import ConfigParser
from contextlib import redirect_stdout
from kiteconnect import KiteConnect
from io import StringIO
from time import sleep
from pyotp import TOTP
import pyperclip as clip
import webbrowser

config = ConfigParser()
config.read('config.ini')
zerodha = config['zerodha']

totp_auth = TOTP(zerodha['totp_key'])
kite = KiteConnect(zerodha['api_key'])

totp = totp_auth.now()
clip.copy(totp)
print(f'TOTP {totp} has been copied to system clipboard')
with redirect_stdout(StringIO()):
    webbrowser.open(kite.login_url())
sleep(1)
request_token = input('Please enter request token after logging in from your browser\n> ')

data = kite.generate_session(request_token, api_secret=zerodha['api_secret'])
kite.set_access_token(data['access_token'])
