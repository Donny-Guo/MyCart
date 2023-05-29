from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import yaml
# import time
# References: https://medium.com/@kikigulab/how-to-automate-opening-and-login-to-websites-with-python-6aeaf1f6ae98

conf = yaml.safe_load(open('loginDetails.yml'))
phone_number = conf['instacart_user']['email']
password = conf['instacart_user']['password']

# Set up Selenium   
service = Service('/usr/local/bin/chromedriver_mac_arm64/chromedriver')  # Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
# options = Options()
# options.add_argument('--headless')  # Run Chrome in headless mode, without opening a window
driver = webdriver.Chrome(service=service)

def login2(url, usernameId, username, passwordId, password, submit_buttonId, login_buttonID):
    driver.get(url)
    driver.find_element(By.CLASS_NAME, login_buttonID).click()
    driver.find_element(By.ID,usernameId).send_keys(phone_number)
    driver.find_element(By.ID,passwordId).send_keys(password)
    driver.find_element(By.NAME, submit_buttonId).click()

login2("https://www.instacart.com/store/lucky-supermarkets/storefront", "email", phone_number, "pass", password, "css-1i23zk9","css-12jtifw")
css-12jtifw
css-1i23zk9


while True:
    flag = input("Enter q to quit: ")
    if flag == 'q':
        driver.close()
        break


