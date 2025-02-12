from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

# Generate a random user agent
ua = UserAgent()
user_agent = ua.random

# Set up Chrome options
options = Options()
options.add_argument(f"user-agent={user_agent}")

# Initialize the Chrome driver
service = Service(r"C:\web drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Now you can navigate to a page
driver.get('https://www.facebook.com/ads/library/?active_status=active&ad_type=political_and_issue_ads&country=PK&media_type=all')

#Add delay
time.sleep(15)

# Close the driver
driver.quit()
