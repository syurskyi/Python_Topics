____ collections ______ defaultdict
_punct _ '.,;?:'
___ _normalize(fragment
    fragment _ fragment.l..
    while len(fragment) > 0 and fragment[-1] in _punct:
        fragment _ fragment[:-1]
    while len(fragment) > 0 and fragment[0] in _punct:
        fragment _ fragment[1:]
    r_ fragment

___ numwords(text
    '''
    Return the number of unique words in a body of text.

    Punctuation and word casing are ignored.
    '''
    words _ set(_normalize(fragment) for fragment in text.split())
    words.discard("")
    r_ len(words)

___ wordcounts(text
    '''
    Return dictionary mapping words to the number of occurences.

    Case is ignored, so each key is the lowercase version of the word.
    '''
    counts _ defaultdict(int)
    for fragment in text.split(
        word _ _normalize(fragment)
        __ word == '':
            continue
        counts[word] +_ 1
    r_ dict(counts)

___ addcounts(existing, new
    '''
    Updates an existing word count dictionary, adding in new values.

    Both existing and new are dicts that map words to counts (ints) - as might
    be returned by wordcounts().

    existing is modified. For each key in new, if that key is in existing, add
    the value in existing.  Else set the value (i.e. treat the count in
    existing as if 0).
    
    If either existing or new are not dictionaries, raise ValueError
    '''
    __ not type(existing) is dict:
        raise ValueError('existing must be a dictionary')
    __ not type(new) is dict:
        raise ValueError('new must be a dictionary')
    for word, count in new.viewitems(
        newcount _ count + existing.get(word, 0)
        existing[word] _ newcount
