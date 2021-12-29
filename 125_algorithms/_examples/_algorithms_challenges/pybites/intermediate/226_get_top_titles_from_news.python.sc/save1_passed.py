from collections import namedtuple
from bs4 import BeautifulSoup
import requests
import re

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
    titles = soup.findAll('span', {'class': 'title'})
    title_list = [entry.get_text().strip() for entry in titles]
    point_list = []
    comment_list = []

    for entry in soup.findAll('span', attrs={'class': 'smaller'}):
        entry = entry.get_text().strip()
        points = re.search(r'(\d*) points', entry)
        comments = re.search(r'(\d*) comments', entry)
        if points:
            point_list.append(int(points.group(1)))
        if comments:
            comment_list.append(int(comments.group(1)))

    output = []
    for entry in zip(title_list, point_list, comment_list):
        output.append(Entry(title=entry[0], points=entry[1], comments=entry[2]))

    return sorted(output, key=lambda x: (x.points, x.comments), reverse=True)[:top]
