____ c.. _______ n..
____ ___ _______ B..
_______ r__
_______ __

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry n..('Entry', 'title points comments')


___ _create_soup_obj(url
    """Need utf-8 to properly parse emojis"""
    resp r__.g.. url)
    resp.encoding "utf-8"
    r.. B..(resp.text, "html.parser")


___ get_top_titles(url, top=5
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup _create_soup_obj(url)
    titles ?.findAll('span', {'class': 'title'})
    title_list [entry.g.. .s.. ___ entry __ titles]
    point_list    # list
    comment_list    # list

    ___ entry __ ?.findAll('span', attrs={'class': 'smaller'}
        entry entry.g.. .s..
        points __.s.. _ (\d*) points', entry)
        comments __.s.. _ (\d*) comments', entry)
        __ points:
            point_list.a..(i..(points.group(1)))
        __ comments:
            comment_list.a..(i..(comments.group(1)))

    output    # list
    ___ entry __ z..(title_list, point_list, comment_list
        ?.a.. Entry(title=entry[0], points=entry[1], comments=entry[2]

    r.. s.. ? , k.._l.... x: (x.points, x.comments), r.._T..[:top]
