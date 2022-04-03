_______ __
____ c.. _______ Counter
_______ u__.r..

# prep
tempfile = __.p...j..('/tmp', 'feed')
u__.r...u..('http://bit.ly/2zD8d8b', tempfile)

w__ o.. tempfile) __ f:
    content = f.r...l..

# start coding
_______ __


___ get_pybites_top_tags(n=10
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    words = __.f..(r'<category>(\w+)</category>', content)
    r.. Counter(words).most_common(10)
