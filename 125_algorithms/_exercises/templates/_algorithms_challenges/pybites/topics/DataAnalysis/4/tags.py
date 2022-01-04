_______ os
____ collections _______ Counter
_______ urllib.request
_______ ___.e__.E__ as ET

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
    root = ET.fromstring(content)
    temp_list    # list
    ___ category __ root.iter('category'):
        temp_list.a..(category.text)
    r.. Counter(temp_list).most_common(n)

print(get_pybites_top_tags(3))