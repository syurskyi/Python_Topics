_______ __
____ c.. _______ C..
_______ u__.r..
_______ ___.e__.E__ __ ET

# prep
tmp = __.getenv("TMP", "/tmp")
tempfile = __.p...j..(tmp, 'feed')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

w__ o.. tempfile) __ f:
    content = f.r...l..


___ get_pybites_top_tags(n=10
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    root = ET.f..(content)
    temp_list    # list
    ___ category __ root.i..('category'
        temp_list.a..(category.text)
    r.. C..(temp_list).most_common(n)

print(get_pybites_top_tags(3))