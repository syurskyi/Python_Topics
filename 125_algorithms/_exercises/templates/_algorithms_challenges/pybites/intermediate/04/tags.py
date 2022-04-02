_______ os
_______ pprint __ pp
____ c.. _______ Counter
_______ urllib.request
_______ ___.e__.E__ __ ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.j..(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

w__ o.. tempfile) __ f:
    content = f.r...l..

___ get_pybites_top_tags(n=10
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    

    counter = Counter()

    root = ET.f..(content)
    
    ___ item __ root[0].f..("item"
        ___ category __ item.f..('category'
            counter[category.text.l..] += 1


    r.. counter.most_common(n)




__ _______ __ _______
    get_pybites_top_tags()





