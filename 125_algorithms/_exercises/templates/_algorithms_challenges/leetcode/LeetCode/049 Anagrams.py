"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
__author__ = 'Danyang'
class Solution:
    ___ anagrams_complicated(self, strs
        """
        sorting
        :param strs: a list of strings
        :return: a list of strings
        """
        temp = list(strs)
        for ind, string in enumerate(temp
            __ string and string!="":  # avoid case of empty string
                string = [char for char in string]
                string.sort()
                string = "".join(string)
                temp[ind] = string


        hash_map = {}
        for ind, string in enumerate(temp
            indexes = hash_map.get(string, [])
            indexes.append(ind)  # side-effect
            hash_map[string] = indexes

        result = []
        for val in hash_map.values(
            __ le.(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] for i in val]
        r_ result

    ___ anagrams(self, strs
        """
        Algorithm: sort string and hash map
        :param strs: a list of strings
        :return: a list of strings
        """
        hash_map = {}
        for ind, string in enumerate(strs
            string = "".join(sorted(string))  # string reversing and sorting are a little different
            __ string not in hash_map:
                hash_map[string] = [ind]
            ____
                hash_map[string].append(ind)
            # indexes = hash_map.get(string, [])
            # indexes.append(ind)  # side-effect
            # hash_map[string] = indexes  # reassign

        result = []
        for val in hash_map.values(
            __ le.(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] for i in val]
        r_ result

__ __name____"__main__":
    Solution().anagrams(["", ""])