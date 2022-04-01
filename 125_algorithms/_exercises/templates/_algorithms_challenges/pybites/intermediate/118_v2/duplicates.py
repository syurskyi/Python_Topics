____ c.. _______ defaultdict
___ get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first occurrence.
       For example in the following list 'is' and 'it'
       occur more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""

    result = s..()
    

    occurences = defaultdict(i..)

    ___ i,word __ e..(words):
        __ word __ occurences:
            result.add(occurences[word])
        ____:
            occurences[word] = i

    

    r.. s..(result)


