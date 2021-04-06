from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
import fakeMail as email
import proxy_service as proxy
import time
import argparse
import os

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")
count = parser.add_argument("count", type=int, default=1, help="number of account creats")

args = parser.parse_args()
ua = UserAgent(verify_ssl=False)
userAgent = ua.random
print(userAgent)
print(args.count)


F = open("namelist.csv", "a")
for x in range(args.count):
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

	driver.get("https://www.instagram.com/accounts/emailsignup/")
	time.sleep(8)

	try:
		cookie = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
	except:
		pass

	#Fill the email value
	email_field = driver.find_element_by_name('emailOrPhone')
	fake_email = email.getFakeMail()
	email_field.send_keys(fake_email)
	print(fake_email)

	# Fill the fullname value
	fullname_field = driver.find_element_by_name('fullName')
	fullName=account.generatingName()
	fullname_field.send_keys(fullName)
	print(fullName)

	# Fill username value
	username_field = driver.find_element_by_name('username')
	name = account.username()
	username_field.send_keys(name)
	print(name)

	# Fill password value
	password_field = driver.find_element_by_name('password')
	password=account.generatePassword()
	password_field.send_keys(password)  # You can determine another password here.
	print(password)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

	line = [fake_email[0], "\t", fullName, "\t", name, "\t", password, "\n"]
	F.writelines(line)

	time.sleep(8)

	#Birthday verification
	driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

	driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

	driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
	time.sleep(3)
	
	fMail = fake_email[0].split("@")
	mailName = fMail[0]
	domain = fMail[1]
	instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
	driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
	time.sleep(10)
	try:
	    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
	    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
	      time.sleep(1)
	      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
	      time.sleep(10)
	      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
	      confInput = driver.find_element_by_name('email_confirmation_code')
	      confInput.send_keys(Keys.CONTROL + "a")
	      confInput.send_keys(Keys.DELETE)
	      confInput.send_keys(instCodeNew, Keys.ENTER)
	except:
	      pass
	      
F.close()
