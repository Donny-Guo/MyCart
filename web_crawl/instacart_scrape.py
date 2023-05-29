from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Selenium
service = Service('/usr/local/bin/chromedriver_mac_arm64/chromedriver')  # Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode, without opening a window
driver = webdriver.Chrome(service=service, options=options)

# Load the web page
url = 'https://www.instacart.com/store/lucky-supermarkets/storefront'
driver.get(url)

# Wait for the page to load and the content to be rendered
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ProductCard')))
html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the desired information
products = soup.find_all('div', class_='ProductCard')
for product in products:
    name = product.find('div', class_='ProductCard-name').text.strip()
    price = product.find('div', class_='ProductCard-price').text.strip()
    print(f'Product: {name} - Price: {price}')
