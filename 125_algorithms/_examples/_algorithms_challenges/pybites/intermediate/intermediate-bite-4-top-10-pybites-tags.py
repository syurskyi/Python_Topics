"""
In this Bite you will get the top 10 blog tags of our PyBites blog
(e.g. python, flask, django, learning).

Our tests suppose you will use a collections.Counter and we loaded a static
copy of our feed so we can predictably test your code. The Pybites tags will
need to be parsed from the xml tags within each (hint: you do not need an xml parser for this task).

What are the PyBites guys most passionate about? See the tests and you'll know the answer.
Then code your solution to make them pass.

Keep calm and code in Python! :)
"""

import os
from collections import Counter
import urllib.request
import re

# prep
DIR = os.getenv('TMP', '/tmp')
FILENAME = "feed.txt"
tempfile = os.path.join(DIR, FILENAME)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    match = re.findall(r'<category>([a-z]+)<\/category>', content)
    c = Counter(match)
    return(c.most_common(10))

get_pybites_top_tags()