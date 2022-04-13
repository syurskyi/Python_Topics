____ c.. _______ n..
_______ __

____ ___ _______ B..
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
    r.. B..(resp.text, "html.parser")


___ get_top_titles(url, top=5
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup _create_soup_obj(url)

    
    entries    # list
    rows ?.f.. "tr",id=T..)
    

    get_number l.... s: i..(__.s.. _ \d+',s).group


    ___ row __ rows:
        links row.s.. 'span.title a')
        title_text links[0].g.. s..=T..)
        link_text ''
        __ l..(links) > 1:
            link_text links[1].g.. s..=T..)
            link_text f" ({link_text})"


        title_text f"{title_text}{link_text}"


        next_row row.find_next_sibling('tr')

        points next_row.s.. 'span.controls > span.smaller').g.. )

        points get_number(points)



        comments next_row.s.. 'span.naturaltime a').g.. s..=T..)

        comments get_number(comments)


        entry Entry(title_text,points,comments)
        entries.a..(entry)


    entries.s..(r.._T..k.._l.... x: (x.points,x.comments

    r.. entries[:top]

















