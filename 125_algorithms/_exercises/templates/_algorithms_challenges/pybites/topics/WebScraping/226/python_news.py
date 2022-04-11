____ c.. _______ n..

____ bs4 _______ BeautifulSoup
_______ r__

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry n..('Entry', 'title points comments')


___ _create_soup_obj(url
    """Need utf-8 to properly parse emojis"""
    resp r__.g.. url)
    resp.encoding "utf-8"
    r.. BeautifulSoup(resp.text, "html.parser")


___ get_top_titles(url, top=5
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup _create_soup_obj(url)
    # your code ...
    title_list    # list
    news_all soup.find_all('span', {'class': 'title'})
    news_points_all soup.find_all('span', {'class': 'controls'})
    ___ i __ r..(l..(news_all:
        meta news_points_all[i].span.text.s...s..
        title_list.a..(Entry(news_all[i].get_text().s.., i..(meta[0]), i..(meta[-2])))
    title_list s..(title_list, key=l.... x: (x.points, x.comments), r.._T..
    r.. [title_list[i] ___ i __ r..(top)]


print(get_top_titles('https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'