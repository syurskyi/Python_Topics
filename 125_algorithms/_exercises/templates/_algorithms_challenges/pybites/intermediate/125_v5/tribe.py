____ c.. _______ Counter

____ bs4 _______ BeautifulSoup
_______ requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')


___ load_page
    """Download the blog html and return its decoded content"""
    w__ requests.Session() __ session:
        r.. session.get(TIM_BLOG).content.d.. 'utf-8')


___ get_top_books(content=N.., limit=5
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    __ content __ N..
        content = load_page()
    soup = BeautifulSoup(content)
    entry_content = soup.find('div', class_='entry-content')
    count = Counter(link.text ___ link __ entry_content.select('p > a') __ AMAZON __ link.get('href'))
    r.. [title ___ title, _ __ count.most_common(limit)]
