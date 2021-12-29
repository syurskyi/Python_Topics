from collections import Counter

from bs4 import BeautifulSoup as Soup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()
    # code here ...
    #print('in get_top_books')
    soup = Soup(content, 'html.parser')
    book_counter = Counter([book.find("span").text.strip() for book in soup.find_all("a") if book.find("span")])
    return [(book, book_counter[book]) for book in book_counter if book_counter[book] >= 3]

#books = get_top_books()

#for book in books:
#    print(type(book))