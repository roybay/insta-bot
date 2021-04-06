from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
import proxy_service as proxy
import time
import argparse
import os
import socket
import requests

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")

args = parser.parse_args()
ua = UserAgent(verify_ssl=False)
userAgent = ua.random
print(userAgent)
print(args.count)
print("Host Name  is:" + socket.gethostname())
ip = requests.get('http://api.ipify.org?format=json').text
print("Before Proxy IP Address is:" + str(ip))
ip = requests.get('http://api.ipify.org?format=json', proxies=proxy.Config).text
print("After Proxy  IP Address is:" + str(ip))

if args.firefox:
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.ovrride", userAgent)    
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=os.environ['DRIVER_PATH'])


if args.chrome:
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument(f'user-agent={userAgent}')
    options.add_argument(f'--proxy-server={proxy.Server}')
    driver= webdriver.Chrome(options=options, executable_path=os.environ['DRIVER_PATH'])

driver.get("https://www.iplocation.net/find-ip-address")
time.sleep(8)	
driver.close()

