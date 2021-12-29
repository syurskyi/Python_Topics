class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    ___ Permutation(self, A, B):
        __ A __ '' a.. B __ '':
            r.. True
        __ n.. A o. n.. B:
            r.. False

        cnts = {}
        ___ char __ A:
            cnts[char] = cnts.get(char, 0) + 1
        ___ char __ B:
            __ char n.. __ cnts o. cnts[char] __ 0:
                r.. False
            cnts[char] -= 1
        ___ cnt __ cnts.values():
            __ cnt != 0:
                r.. False

        r.. True
