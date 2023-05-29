from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import yaml
# import time
# References: https://medium.com/@kikigulab/how-to-automate-opening-and-login-to-websites-with-python-6aeaf1f6ae98

conf = yaml.safe_load(open('loginDetails.yml'))
phone_number = conf['fb_user']['phone_number']
password = conf['fb_user']['password']

# Set up Selenium   
service = Service('/usr/local/bin/chromedriver_mac_arm64/chromedriver')  # Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
# options = Options()
# options.add_argument('--headless')  # Run Chrome in headless mode, without opening a window
driver = webdriver.Chrome(service=service)

def login(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element(By.ID,usernameId).send_keys(phone_number)
    driver.find_element(By.ID,passwordId).send_keys(password)
    driver.find_element(By.NAME, submit_buttonId).click()

login("https://www.facebook.com/", "email", phone_number, "pass", password, "login")

while True:
    flag = input("Enter q to quit: ")
    if flag == 'q':
        driver.close()
        break
