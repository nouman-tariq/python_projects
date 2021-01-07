from bs4 import BeautifulSoup
import urllib.request
import re
import requests

nida_mag_page = urllib.request.urlopen("https://tanzeem.org/multimedia/magazines/nida-e-khilafat/")
soup = BeautifulSoup(nida_mag_page, 'html.parser')

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


latest_mag_html = urllib.request.urlopen(magazine_links[0])
soup = BeautifulSoup(latest_mag_html, 'html.parser')

download_add = soup.find_all('a', attrs={'class': 'download-btn'})
download_link = download_add[0].attrs['href']

download_mag = urllib.request.urlopen(download_link)
magazine = open('nida.pdf', 'wb')
magazine.write(download_mag.read())
magazine.close()