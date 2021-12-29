class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    ___ Permutation(self, A, B):
        __ A is '' and B is '':
            return True
        __ not A or not B:
            return False

        cnts = {}
        for char in A:
            cnts[char] = cnts.get(char, 0) + 1
        for char in B:
            __ char not in cnts or cnts[char] == 0:
                return False
            cnts[char] -= 1
        for cnt in cnts.values():
            __ cnt != 0:
                return False

        return True
