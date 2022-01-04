_______ os
____ collections _______ Counter
_______ urllib.request

# prep
tempfile = os.path.j..('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

w__ open(tempfile) __ f:
    content = f.read().l..

# start coding
_______ __


___ get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    words = __.f..(r'<category>(\w+)</category>', content)
    r.. Counter(words).most_common(10)
