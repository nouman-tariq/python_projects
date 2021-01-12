# git clone https://github.com/bisguzar/twitter-scraper.git
# cd twitter-scraper
# sudo python3 setup.py install
# pip3 install twitter_scraper


# from twitter_scraper import get_tweets
# for tweet in get_tweets('_M_Nouman_Tariq', pages=3):
#     print(tweet['text'])

# # from twitter_scraper import get_trends
# # get_trends()

from bs4 import BeautifulSoup
import urllib.request

twitter_page = urllib.request.urlopen("https://twitter.com/")
page = BeautifulSoup(twitter_page, 'html.parser')

print(page.prettify())