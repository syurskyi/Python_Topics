"""
Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
__author__ = 'Danyang'
c_ Solution:
    digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    ___ letterCombinations  d..):
        """
        DFS
        :param digits: str
        :return: a list of strings, [s1, s2]
        """
        result    # list
        dfs_traverse(d.., "", result)
        r.. result

    ___ dfs_traverse  string_seq, current, result):
        __ n.. string_seq:
            result.a..(current)
            r..

        ___ letter __ digit2letters[string_seq[0]]:
            dfs_traverse(string_seq[1:], current+letter, result)


__ _____ __ ____
    print Solution().letterCombinations("23")