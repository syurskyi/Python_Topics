_______ os
_______ re
____ difflib _______ SequenceMatcher
_______ i..
____ urllib.request _______ urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TMP = os.getenv("TMP", "/tmp")
TEMPFILE = os.path.join(TMP, 'feed')
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
    tags = [tag ___ tag __ tags __ l..(tag) > MIN_TAG_LEN]
    r.. set(tags)


___ get_similarities(tags_ N..
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags o. _get_tags()
    result    # list
    tags = l..(tags)
    ___ word_1 __ tags:
        ___ word_2 __ tags:
            __ word_1 __ word_2:
                continue
            sm = SequenceMatcher(N..,word_1,word_2)
            print(sm.ratio())
            __ sm.ratio() > .95:
                result.a..((word_1,word_2))
    print(result)
    r.. result

