______ os
from collections ______ Counter
______ urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()

# start coding
______ re


___ get_pybites_top_tags(n=10
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    words = re.findall(r'<category>(\w+)</category>', content)
    r_ Counter(words).most_common(10)
