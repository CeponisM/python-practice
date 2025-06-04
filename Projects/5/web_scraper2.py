# ### 5. Simple Web Scraper

# **Description**: Extract data from a website that contais JaveScript.

# **Practice Goals**:
# - Working with external libraries
# - HTTP requests and response handling
# - HTML parsing and data extraction

# Wanted a web-scraper that could parse my website

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup headless browser
options = Options()
options.add_argument('--headless')  # run in background
options.add_argument('--disable-gpu')

# Point to ChromeDriver
driver = webdriver.Chrome(options=options)

# Load the site
driver.get("https://MCeponis.com")

# Give time for JavaScript to load
time.sleep(3)

# Find all project titles
project_titles = driver.find_elements(By.CLASS_NAME, "project-title")

print("📝 Project Titles:")
for elem in project_titles:
    print("-", elem.text.strip())

# Clean up
driver.quit()