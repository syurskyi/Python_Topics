"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ anagrams_complicated(self, strs):
        """
        sorting
        :param strs: a list of strings
        :return: a list of strings
        """
        temp = l..(strs)
        ___ ind, string __ e..(temp):
            __ string a.. string!="":  # avoid case of empty string
                string = [char ___ char __ string]
                string.s..()
                string = "".j..(string)
                temp[ind] = string


        hash_map    # dict
        ___ ind, string __ e..(temp):
            indexes = hash_map.get(string, [])
            indexes.a..(ind)  # side-effect
            hash_map[string] = indexes

        result    # list
        ___ val __ hash_map.v..
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
        hash_map    # dict
        ___ ind, string __ e..(strs):
            string = "".j..(s..(string))  # string reversing and sorting are a little different
            __ string n.. __ hash_map:
                hash_map[string] = [ind]
            ____:
                hash_map[string].a..(ind)
            # indexes = hash_map.get(string, [])
            # indexes.append(ind)  # side-effect
            # hash_map[string] = indexes  # reassign

        result    # list
        ___ val __ hash_map.v..
            __ l..(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] ___ i __ val]
        r.. result

__ __name____"__main__":
    Solution().anagrams(["", ""])