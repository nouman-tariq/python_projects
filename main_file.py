from bs4 import BeautifulSoup
import urllib.request
import re

# Link of the website and the magazine
nida_mag_page = urllib.request.urlopen("https://tanzeem.org/multimedia/magazines/nida-e-khilafat/")
soup = BeautifulSoup(nida_mag_page, 'html.parser')


# extracting all of the links, this page contains
total_links = []
magazine_links = []
for link in soup.find_all('a'):
    total_links.append(link.get('href'))


# separating the links which contains magaznies
for link in total_links:
    magazine_add = re.search('.*magazines/[0-9].*', link)
    if magazine_add:
        magazine_links.append(magazine_add.string)


# opening the latest magazine
latest_mag_html = urllib.request.urlopen(magazine_links[0])
soup = BeautifulSoup(latest_mag_html, 'html.parser')


# downloading the latest magazine
download_address = soup.find_all('a', attrs={'class': 'download-btn'})
download_link = download_address[0].attrs['href']
download_mag = urllib.request.urlopen(download_link)


# saving the downloaded magazine
magazine = open('nida.pdf', 'wb')
magazine.write(download_mag.read())
magazine.close()