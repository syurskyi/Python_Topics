____ collections ______ defaultdict
_punct _ '.,;?:'
___ _normalize(fragment
    fragment _ fragment.l..
    while len(fragment) > 0 an. fragment[-1] __ _punct:
        fragment _ fragment[:-1]
    while len(fragment) > 0 an. fragment[0] __ _punct:
        fragment _ fragment[1:]
    r_ fragment

___ numwords(text
    '''
    Return the number of unique words in a body of text.

    Punctuation and word casing are ignored.
    '''
    words _ set(_normalize(fragment) ___ fragment __ text.split())
    words.discard("")
    r_ len(words)

___ wordcounts(text
    '''
    Return dictionary mapping words to the number of occurences.

    Case is ignored, so each key is the lowercase version of the word.
    '''
    counts _ defaultdict(__.)
    ___ fragment __ text.split(
        word _ _normalize(fragment)
        __ word __ '':
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
    __ no. type(existing) __ dict:
        r_ V..('existing must be a dictionary')
    __ no. type(new) __ dict:
        r_ V..('new must be a dictionary')
    ___ word, count __ new.viewitems(
        newcount _ count + existing.get(word, 0)
        existing[word] _ newcount
