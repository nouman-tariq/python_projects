from bs4 import BeautifulSoup
import urllib.request

html_page = urllib.request.urlopen("https://tanzeem.org/multimedia/magazines/nida-e-khilafat/")
soup = BeautifulSoup(html_page, features='html.parser')

for a in soup.findAll('div', attrs={'class': 'category-list'}):
    print(a.prettify)
