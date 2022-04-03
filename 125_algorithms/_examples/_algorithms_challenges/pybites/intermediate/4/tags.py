import os
from collections import Counter
import u__.r..
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()
    root = ET.fromstring(content)
    categories = [category.text for category in root.iter("category")]


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = Counter()
    tags.update(categories)
    return tags.most_common()[:n]

#print(get_pybites_top_tags())