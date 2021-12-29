import os
import pprint as pp
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

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
    

    counter = Counter()

    root = ET.fromstring(content)
    
    for item in root[0].findall("item"):
        for category in item.findall('category'):
            counter[category.text.lower()] += 1


    return counter.most_common(n)




__ __name__ == "__main__":
    get_pybites_top_tags()





