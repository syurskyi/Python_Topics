_______ os
____ collections _______ Counter
_______ urllib.request
_______ xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


___ get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    root = ET.fromstring(content)
    temp_list    # list
    ___ category __ root.iter('category'):
        temp_list.a..(category.text)
    r.. Counter(temp_list).most_common(n)

print(get_pybites_top_tags(3))