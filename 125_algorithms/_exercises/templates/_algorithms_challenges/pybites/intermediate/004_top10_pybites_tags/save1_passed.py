_______ os
____ c.. _______ Counter
_______ urllib.request
_______ __

# prep
tempfile = os.path.j..('/tmp', 'feed')
urllib.request.urlretrieve(
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
