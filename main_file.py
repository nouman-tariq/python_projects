from bs4 import BeautifulSoup
import urllib.request
import re


html_page = urllib.request.urlopen("https://tanzeem.org/multimedia/magazines/nida-e-khilafat/")
soup = BeautifulSoup(html_page, features='html.parser')

# mag_class = soup.find_all('div', attrs={'class': 'category-list'})
# print(mag_class)

total_links = []
magazine_links = []
for link in soup.find_all('a'):
    total_links.append(link.get('href'))

for link in total_links:
    magazine_add = re.search('.*magazines/[0-9].*', link)
    if magazine_add:
        magazine_links.append(magazine_add.string)

print(magazine_links)