____ c.. _______ C..

____ bs4 _______ BeautifulSoup __ Soup
_______ r__

AMAZON "amazon.com"
# static copy
TIM_BLOG ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT 3


___ load_page
    """Download the blog html and return its decoded content"""
    w__ r__.S.. __ session:
        r.. session.g.. TIM_BLOG).content.d.. 'utf-8')


___ get_top_books(content_ N..
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    __ content __ N..
        content load_page()
    # code here ...
    #print('in get_top_books')
    soup Soup(content, 'html.parser')
    book_counter C..([book.find("span").text.s.. ___ book __ soup.find_all("a") __ book.find("span")])
    r.. [(book, book_counter[book]) ___ book __ book_counter __ book_counter[book] >_ 3]

#books = get_top_books()

#for book in books:
#    print(type(book))