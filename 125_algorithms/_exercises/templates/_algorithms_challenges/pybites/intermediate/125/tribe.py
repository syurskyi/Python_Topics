____ c.. _______ C..

____ ___ _______ B..
_______ ___
_______ r__

AMAZON "amazon.com"
# static copy
TIM_BLOG ('https://bites-data.s3.us-east-2.amazonaws.com/tribe-mentors-books.html')
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
    
    soup B..(content, "html.parser")
    
    amazon_books    # list
    ___ link __ ?.f.. "a"
        __ "amazon" __ link.g.. "href"
            amazon_books.a..([link.g.. .s...s..("\n")])

    amazon_books_counter C..()
    ___ book __ amazon_books:
        amazon_books_counter.update(book)

    r.. [(key, value) ___ key, value __ amazon_books_counter.i.. __ value >_ MIN_COUNT]


__ _______ __ _______
    print(get_top_books