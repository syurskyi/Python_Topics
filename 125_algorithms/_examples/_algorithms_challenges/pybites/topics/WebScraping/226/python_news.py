from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    # your code ...
    title_list = []
    news_all = soup.find_all('span', {'class': 'title'})
    news_points_all = soup.find_all('span', {'class': 'controls'})
    for i in range(len(news_all)):
        meta = news_points_all[i].span.text.strip().split()
        title_list.append(Entry(news_all[i].get_text().strip(), int(meta[0]), int(meta[-2])))
    title_list = sorted(title_list, key=lambda x: (x.points, x.comments), reverse=True)
    return [title_list[i] for i in range(top)]


print(get_top_titles('https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'))