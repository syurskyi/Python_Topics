from collections import Counter
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

    soup = BeautifulSoup(content, 'html.parser')
    right_table = soup.find('div', {'class': 'entry-content'})

    books = [row.text 
             for row in right_table.select('a[href*=amazon]')]
    c = Counter(books)
    
    books_final = []
    count = []
    for letter in c:
        __ c[letter] >= MIN_COUNT:
            books_final.append(letter)
            count.append(c[letter])

    return sorted(list(zip(books_final, count)), 
                  key=lambda tup: tup[1], reverse=True)