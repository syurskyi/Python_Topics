_______ os
____ collections _______ Counter
_______ urllib.request
_______ ___.e__.E__ __ ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.j..(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

w__ open(tempfile) __ f:
    content = f.read().l..
    root = ET.f..(content)
    categories = [category.text ___ category __ root.i..("category")]


___ get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = Counter()
    tags.update(categories)
    r.. tags.most_common()[:n]

#print(get_pybites_top_tags())