_______ __
____ c.. _______ Counter
_______ u__.r..
_______ __

# prep
tempfile = __.p...j..('/tmp', 'feed')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

w__ o.. tempfile) __ f:
    content = f.r...l..


___ get_pybites_top_tags(n=10
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    m.. = __.f..(r'<category>(.*?)</category>', content)
    r.. Counter(m..).most_common(n)
