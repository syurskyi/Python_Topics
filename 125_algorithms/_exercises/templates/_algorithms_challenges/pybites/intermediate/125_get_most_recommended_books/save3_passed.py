____ c.. _______ C..
____ bs4 _______ BeautifulSoup
_______ r__
_______ __

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


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
        content = load_page()

    soup = BeautifulSoup(content, 'html.parser')
    right_table = soup.find('div', {'class': 'entry-content'})

    books = [row.text.s..
             ___ row __ right_table.find_all(
            'a', href=__.c..(AMAZON]
    c = C..(books)

    books_final    # list
    count    # list
    ___ letter __ c:
        __ c[letter] >= MIN_COUNT:
            books_final.a..(letter.s..
            count.a..(c[letter])

    r.. s..(l..(z..(books_final, count,
                  key=l.... tup: tup[1], r.._T..