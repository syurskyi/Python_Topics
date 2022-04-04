_______ __
____ c.. _______ C..
_______ u__.r..
_______ ___.e__.E__ __ ET

# prep
tmp = __.g..("TMP", "/tmp")
tempfile = __.p...j..(tmp, 'feed')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

w__ o.. tempfile) __ f:
    content = f.r...l..
    root = ET.f..(content)
    categories = [category.text ___ category __ root.i..("category")]


___ get_pybites_top_tags(n=10
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = C..()
    tags.update(categories)
    r.. tags.m.. :?

#print(get_pybites_top_tags())