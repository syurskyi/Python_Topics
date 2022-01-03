_______ os
_______ pprint as pp
____ collections _______ Counter
_______ urllib.request
_______ xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.j..(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().l..

___ get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    

    counter = Counter()

    root = ET.fromstring(content)
    
    ___ item __ root[0].findall("item"):
        ___ category __ item.findall('category'):
            counter[category.text.l..] += 1


    r.. counter.most_common(n)




__ __name__ __ "__main__":
    get_pybites_top_tags()





