"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
__author__ = 'Danyang'
class Solution:
    ___ anagrams_complicated(self, strs):
        """
        sorting
        :param strs: a list of strings
        :return: a list of strings
        """
        temp = l..(strs)
        ___ ind, string __ enumerate(temp):
            __ string and string!="":  # avoid case of empty string
                string = [char ___ char __ string]
                string.sort()
                string = "".join(string)
                temp[ind] = string


        hash_map = {}
        ___ ind, string __ enumerate(temp):
            indexes = hash_map.get(string, [])
            indexes.a..(ind)  # side-effect
            hash_map[string] = indexes

        result    # list
        ___ val __ hash_map.values():
            __ l..(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] ___ i __ val]
        r.. result

    ___ anagrams(self, strs):
        """
        Algorithm: sort string and hash map
        :param strs: a list of strings
        :return: a list of strings
        """
        hash_map = {}
        ___ ind, string __ enumerate(strs):
            string = "".join(s..(string))  # string reversing and sorting are a little different
            __ string n.. __ hash_map:
                hash_map[string] = [ind]
            ____:
                hash_map[string].a..(ind)
            # indexes = hash_map.get(string, [])
            # indexes.append(ind)  # side-effect
            # hash_map[string] = indexes  # reassign

        result    # list
        ___ val __ hash_map.values():
            __ l..(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] ___ i __ val]
        r.. result

__ __name____"__main__":
    Solution().anagrams(["", ""])