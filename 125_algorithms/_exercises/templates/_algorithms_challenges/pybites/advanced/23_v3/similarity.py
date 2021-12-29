import os
import re
from difflib import SequenceMatcher
from itertools import permutations
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
    TEMPFILE
)


___ _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags __ len(tag) > MIN_TAG_LEN]
    return set(tags)


___ get_similarities(tags_ N..
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # do your thing ...
    for a, b in permutations(tags, 2):
        __ SequenceMatcher(a=a, b=b).ratio() >= SIMILAR:
            yield a, b
