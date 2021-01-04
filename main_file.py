from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
browser.get('https://tanzeem.org/multimedia/magazines/')
# print('Title: %s' % browser.title)
# browser.quit()
