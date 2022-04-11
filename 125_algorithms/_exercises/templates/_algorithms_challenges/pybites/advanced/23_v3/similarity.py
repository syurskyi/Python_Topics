_______ __
_______ __
____ difflib _______ SequenceMatcher
____ i.. _______ permutations
____ u__.r.. _______ u..

# prep
TAG_HTML __.c..(r'<category>([^<]+)</category>')
TEMPFILE __.p...j..('/tmp', 'feed')
MIN_TAG_LEN 10
IDENTICAL 1.0
SIMILAR 0.95

u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
    TEMPFILE
)


___ _get_tags(tempfile=TEMPFILE
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    w__ o.. ? __ f
        content f.r...l..
    # take a small subset to keep it performant
    tags TAG_HTML.f..(content)
    tags [tag ___ tag __ tags __ l..(tag) > MIN_TAG_LEN]
    r.. s..(tags)


___ get_similarities(tags_ N..
    """Should return a list of similar tag pairs (tuples)"""
    tags tags o. _get_tags()
    # do your thing ...
    ___ a, b __ p.. tags, 2
        __ SequenceMatcher(a=a, b=b).ratio() >_ SIMILAR:
            y.. a, b
