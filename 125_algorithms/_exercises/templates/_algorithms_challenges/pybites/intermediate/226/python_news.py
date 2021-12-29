from collections import namedtuple
import re

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


___ _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


___ get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    
    entries = []
    rows = soup.find_all("tr",id=True)
    

    get_number = lambda s: int(re.search(r'\d+',s).group())


    for row in rows:
        links = row.select('span.title a')
        title_text = links[0].getText(strip=True)
        link_text = ''
        __ len(links) > 1:
            link_text = links[1].getText(strip=True)
            link_text = f" ({link_text})"


        title_text = f"{title_text}{link_text}"


        next_row = row.find_next_sibling('tr')

        points = next_row.select_one('span.controls > span.smaller').getText()

        points = get_number(points)



        comments = next_row.select_one('span.naturaltime a').getText(strip=True)

        comments = get_number(comments)


        entry = Entry(title_text,points,comments)
        entries.append(entry)


    entries.sort(reverse=True,key=lambda x: (x.points,x.comments))

    return entries[:top]

















