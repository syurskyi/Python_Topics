from collections import Counter

import re
from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


___ load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


___ get_top_books(content_ N..
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    __ content is None:
        content = load_page()

    counts = Counter()
    soup = BeautifulSoup(content,'html.parser')

    links =  soup.find_all('a',href=re.compile(r'amazon.com'))

    for link in links:
        title = link.getText(strip=True)
        counts[title] += 1

    

    return [value for value in counts.items() __ value[1] >= MIN_COUNT]


    # code here ...
