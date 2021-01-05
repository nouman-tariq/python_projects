from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
browser.get('https://tanzeem.org/multimedia/magazines/')
# print('Title: %s' % browser.title)

content = browser.page_source
soup = BeautifulSoup(content, features='html.parser')
# print(soup.prettify())

for a in soup.findAll('div', attrs={'class': "col-sm-12 category-items all-items"}):
    print(a)

browser.quit()
