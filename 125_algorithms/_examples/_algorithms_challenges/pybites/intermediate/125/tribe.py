from collections import Counter

from bs4 import BeautifulSoup
import bs4
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/tribe-mentors-books.html')
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
    
    soup = BeautifulSoup(content, "html.parser")
    
    amazon_books = []
    for link in soup.find_all("a"):
        if "amazon" in link.get("href"):
            amazon_books.append([link.get_text().strip().strip("\n")])

    amazon_books_counter = Counter()
    for book in amazon_books:
        amazon_books_counter.update(book)

    return [(key, value) for key, value in amazon_books_counter.items() if value >= MIN_COUNT]


if __name__ == "__main__":
    print(get_top_books())