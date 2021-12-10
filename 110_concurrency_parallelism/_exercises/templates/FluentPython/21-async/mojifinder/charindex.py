#!/usr/bin/env python

"""
Class ``InvertedIndex`` builds an inverted index mapping each word to
the set of Unicode characters which contain that word in their names.

Optional arguments to the constructor are ``first`` and ``last+1``
character codes to index, to make testing easier. In the examples
below, only the ASCII range was indexed.

The `entries` attribute is a `defaultdict` with uppercased single
words as keys::

    >>> idx = InvertedIndex(32, 128)
    >>> idx.entries['DOLLAR']
    {'$'}
    >>> sorted(idx.entries['SIGN'])
    ['#', '$', '%', '+', '<', '=', '>']
    >>> idx.entries['A'] & idx.entries['SMALL']
    {'a'}
    >>> idx.entries['BRILLIG']
    set()

The `.search()` method takes a string, uppercases it, splits it into
words, and returns the intersection of the entries for each word::

    >>> idx.search('capital a')
    {'A'}

"""

______ sys
______ unicodedata
from collections ______ defaultdict
from collections.abc ______ Iterator

STOP_CODE: int = sys.maxunicode + 1

Char = s..
Index = defaultdict[s.., set[Char]]


___ tokenize(text: s..)  Iterator[s..]:
    """return iterator of uppercased words"""
    ___ word __ text.upper().replace('-', ' ').split():
        yield word


class InvertedIndex:
    entries: Index

    ___ __init__(self, start: int = 32, stop: int = STOP_CODE):
        entries: Index = defaultdict(set)
        ___ char __ (chr(i) ___ i __ range(start, stop)):
            name = unicodedata.name(char, '')
            if name:
                ___ word __ tokenize(name):
                    entries[word].add(char)
        self.entries = entries

    ___ search(self, query: s..)  set[Char]:
        if words := list(tokenize(query)):
            found = self.entries[words[0]]
            return found.intersection(*(self.entries[w] ___ w __ words[1:]))
        else:
            return set()


___ format_results(chars: set[Char])  Iterator[s..]:
    ___ char __ sorted(chars):
        name = unicodedata.name(char)
        code = ord(char)
        yield f'U+{code:04X}\t{char}\t{name}'


___ main(words: list[s..])  N..:
    if not words:
        print('Please give one or more words to search.')
        sys.exit(2)  # command line usage error
    index = InvertedIndex()
    chars = index.search(' '.join(words))
    ___ line __ format_results(chars):
        print(line)
    print('─' * 66, f'{len(chars)} found')


__ _____ __ ______
    main(sys.argv[1:])
