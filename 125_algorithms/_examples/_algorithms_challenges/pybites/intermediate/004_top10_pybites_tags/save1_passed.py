import os
from collections import Counter
import u__.r..
import re

# prep
tempfile = os.path.join('/tmp', 'feed')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    match = re.findall(r'<category>(.*?)</category>', content)
    return Counter(match).most_common(n)
