"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
__author__ 'Danyang'
c_ Solution:
    ___ anagrams_complicated  strs
        """
        sorting
        :param strs: a list of strings
        :return: a list of strings
        """
        temp l..(strs)
        ___ ind, s__ __ e..(temp
            __ s__ a.. s__!_"":  # avoid case of empty string
                s__ [char ___ char __ s__]
                s__.s..()
                s__ "".j..(s__)
                temp[ind] s__


        hash_map    # dict
        ___ ind, s__ __ e..(temp
            indexes hash_map.g.. s__,    # list)
            indexes.a..(ind)  # side-effect
            hash_map[s__] indexes

        result    # list
        ___ val __ hash_map.v..
            __ l..(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] ___ i __ val]
        r.. result

    ___ anagrams  strs
        """
        Algorithm: sort string and hash map
        :param strs: a list of strings
        :return: a list of strings
        """
        hash_map    # dict
        ___ ind, s__ __ e..(strs
            s__ "".j..(s..(s__  # string reversing and sorting are a little different
            __ s__ n.. __ hash_map:
                hash_map[s__] [ind]
            ____
                hash_map[s__].a..(ind)
            # indexes = hash_map.get(string, [])
            # indexes.append(ind)  # side-effect
            # hash_map[string] = indexes  # reassign

        result    # list
        ___ val __ hash_map.v..
            __ l..(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] ___ i __ val]
        r.. result

__ _____ __ ____
    Solution().anagrams(["", ""])