______ re
from collections ______ namedtuple

______ requests
from bs4 ______ BeautifulSoup

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


___ _create_soup_obj(url
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    r_ BeautifulSoup(resp.text, "html.parser")


___ get_top_titles(url, top=5
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    article_list = soup.select('span.title')

    articles = []
    for article in article_list:
        # Nasty hack, knowing the structure of the page:
        stats = article.parent.parent.parent.next_sibling.next_sibling.text
        # Get the number of points and comments, but don't check for plurals… just in case!
        extract = re.search(r'(\d+) point.* (\d+) comment', stats, re.DOTALL)
        articles.append(Entry(article.text.strip(), int(extract.group(1)), int(extract.group(2))))

    r_ sorted(articles, key=lambda x: -(x.points + x.comments / 1000))[:top]
