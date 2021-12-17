from configparser import ConfigParser
from kiteconnect import KiteConnect
from pyotp import TOTP
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import parse_qs, urlparse

chrome_path = ChromeDriverManager().install()

config = ConfigParser()
config.read('config.ini')
zerodha = config['zerodha']

totp_auth = TOTP(zerodha['totp_key'])
kite = KiteConnect(zerodha['api_key'])

totp = totp_auth.now()

with Chrome(chrome_path) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(kite.login_url())
    wait.until(EC.presence_of_element_located((By.ID, 'userid'))).send_keys(zerodha['user_id'])
    driver.find_element(By.ID, 'password').send_keys(zerodha['password'])
    driver.find_element(By.CSS_SELECTOR, '.login-form button[type="submit"]').click()
    wait.until(EC.presence_of_element_located((By.ID, 'totp'))).send_keys(totp)
    driver.find_element(By.CSS_SELECTOR, '.login-form button[type="submit"]').click()
    wait.until(lambda driver: 'request_token' in driver.current_url)
    url = driver.current_url

request_token = parse_qs(urlparse(url).query)['request_token'][0]

data = kite.generate_session(request_token, api_secret=zerodha['api_secret'])
kite.set_access_token(data['access_token'])
