from collections ______ defaultdict


___ get_duplicate_indices(words
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    wordlist = defaultdict(list)
    ___ pos, word in enumerate(words
        wordlist[word].append(pos)
    r_ sorted(p[0] ___ p in wordlist.values() __ le.(p) > 1)
