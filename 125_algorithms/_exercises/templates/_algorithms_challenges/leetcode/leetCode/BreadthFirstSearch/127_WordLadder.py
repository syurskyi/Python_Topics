#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ ladderLength  beginWord, endWord, wordList
        """
        Breadth First Search
        When build the adjacency tree, skip the visited word
        """
        __ beginWord __ endWord:
            r_ 1
        cur_level = [beginWord]
        next_level   # list
        visited_word _ # dict
        visited_word[beginWord] = 1
        length = 0
        _____ cur_level:
            length += 1
            ___ cur_word __ cur_level:
                cur_len = l..(cur_word)
                # Get the next level
                # When I put "abc...xyz" in the out loop, it just exceeded.
                ___ i __ r..(cur_len
                    pre_word = cur_word[:i]
                    post_word = cur_word[i+1:]
                    ___ j __ "abcdefghijklmnopqrstuvwxyz":
                        next_word = pre_word + j + post_word
                        # Find the endWord
                        __ next_word __ endWord:
                            r_ length + 1
                        ____ (next_word n.. __ visited_word a..
                                next_word __ wordList
                            visited_word[next_word] = 1
                            next_level.a.. next_word)
                        ____
                            pass

            # Scan the next level then
            cur_level = next_level
            next_level   # list
        r_ 0

    """ disapproved, when wordList growth bigger, it may be called too many times
    def is_one_distance(self, word_1, word_2):
        # alert(len(word_1) == len(word_2))
        word_l = len(word_1)
        one_distance = False
        for i in range(word_l):
            if word_1[i] != word_2[i]:
                if not one_distance:
                    one_distance = True
                else:
                    return False

        return one_distance
    """
"""
if __name__ == '__main__':
    sol = Solution()
    print sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print sol.ladderLength("hit", "cog", ["hot", "dot", "doh", "lot", "loh"])
    print sol.ladderLength(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "hig", "hog"])

    print sol.ladderLength(
        "cet", "ism",
        ['cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'get',
         'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm'])
"""
