class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    ___ Permutation(self, A, B
        __ A pa__ '' and B pa__ '':
            r_ True
        __ not A or not B:
            r_ False

        cnts = {}
        ___ char in A:
            cnts[char] = cnts.get(char, 0) + 1
        ___ char in B:
            __ char not in cnts or cnts[char] __ 0:
                r_ False
            cnts[char] -= 1
        ___ cnt in cnts.values(
            __ cnt != 0:
                r_ False

        r_ True
