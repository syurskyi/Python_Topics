____ c.. _______ Counter
____ bs4 _______ BeautifulSoup
_______ requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


___ load_page
    """Download the blog html and return its decoded content"""
    w__ requests.Session() __ session:
        r.. session.get(TIM_BLOG).content.d.. 'utf-8')


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

    books = [row.text 
             ___ row __ right_table.select('a[href*=amazon]')]
    c = Counter(books)
    
    books_final    # list
    count    # list
    ___ letter __ c:
        __ c[letter] >= MIN_COUNT:
            books_final.a..(letter.strip())
            count.a..(c[letter])

    r.. s..(l..(z..(books_final, count)),
                  key=l.... tup: tup[1], r.._T..