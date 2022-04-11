____ c.. _______ C..

_______ __
____ bs4 _______ BeautifulSoup
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

    counts C..()
    soup BeautifulSoup(content,'html.parser')

    links =  soup.find_all('a',href=__.c..(r'amazon.com'

    ___ link __ links:
        title link.getText(s..=T..)
        counts[title] += 1

    

    r.. [value ___ value __ counts.i.. __ value[1] >_ MIN_COUNT]


    # code here ...
