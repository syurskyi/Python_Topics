from collections import defaultdict
_punct = '.,;?:'
def _normalize(fragment):
    fragment = fragment.lower()
    while len(fragment) > 0 and fragment[-1] in _punct:
        fragment = fragment[:-1]
    while len(fragment) > 0 and fragment[0] in _punct:
        fragment = fragment[1:]
    return fragment

def numwords(text):
    '''
    Return the number of unique words in a body of text.

    Punctuation and word casing are ignored.
    '''
    words = set(_normalize(fragment) for fragment in text.split())
    words.discard("")
    return len(words)

def wordcounts(text):
    '''
    Return dictionary mapping words to the number of occurences.

    Case is ignored, so each key is the lowercase version of the word.
    '''
    counts = defaultdict(int)
    for fragment in text.split():
        word = _normalize(fragment)
        if word == '':
            continue
        counts[word] += 1
    return dict(counts)

def addcounts(existing, new):
    '''
    Updates an existing word count dictionary, adding in new values.

    Both existing and new are dicts that map words to counts (ints) - as might
    be returned by wordcounts().

    existing is modified. For each key in new, if that key is in existing, add
    the value in existing.  Else set the value (i.e. treat the count in
    existing as if 0).
    
    If either existing or new are not dictionaries, raise ValueError
    '''
    if not type(existing) is dict:
        raise ValueError('existing must be a dictionary')
    if not type(new) is dict:
        raise ValueError('new must be a dictionary')
    for word, count in new.viewitems():
        newcount = count + existing.get(word, 0)
        existing[word] = newcount
