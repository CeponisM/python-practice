# ### 5. Simple Web Scraper

# **Description**: Extract data from a website using `requests` and `BeautifulSoup`.

# **Practice Goals**:
# - Working with external libraries
# - HTTP requests and response handling
# - HTML parsing and data extraction

# Requires 'pip install requests beautifulsoup4'


# Return first 500 characters of html from a website
import requests

url = "https://mceponis.com"
response = requests.get(url)

print('status code: ', response.status_code)
print('Content', response.text)


# Extracting Title of page
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print('Page Title: ', soup.title.string)