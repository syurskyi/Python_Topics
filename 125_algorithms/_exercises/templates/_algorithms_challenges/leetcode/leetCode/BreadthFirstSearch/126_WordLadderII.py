#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ findLadders  beginWord, endWord, wordlist
        __ beginWord __ endWord:
            r_ [[beginWord]]
        cur_level = [beginWord]
        next_level   # list
        visited_word _ # dict
        visited_word[beginWord] = 1

        # BFS: find whether there are shortest transformation sequence(s)
        find_shortest = False
        self.pre_word_list _ # dict
        _____ cur_level:
            __ find_shortest:
                break
            ___ cur_word __ cur_level:
                cur_len = l..(cur_word)
                # Get the next level
                # When I put "abc...xyz" in the out loop, it just exceeded.
                ___ i __ r..(cur_len
                    pre_word = cur_word[:i]
                    post_word = cur_word[i+1:]
                    ___ j __ "abcdefghijklmnopqrstuvwxyz":
                        next_word = pre_word + j + post_word
                        # Just find one shorttest transformation sequence
                        __ next_word __ endWord:
                            find_shortest = True
                        ____
                            pass
                        __ (next_word n.. __ visited_word and
                                next_word __ wordlist or next_word __ endWord
                            __ next_word n.. __ next_level:
                                next_level.append(next_word)
                            ____
                                pass

                            __ next_word n.. __ self.pre_word_list:
                                self.pre_word_list[next_word] = [cur_word]
                            ____
                                self.pre_word_list[next_word].append(cur_word)
                        ____
                            pass
            ___ w __ next_level:
                visited_word[w] = 1
            # Scan the next level then
            cur_level = next_level
            next_level   # list
        __ find_shortest:
            self.results   # list
            self.dfs_sequences(beginWord, endWord, [endWord])
            r_ self.results
        ____
            r_ []

    """
    Build the path according to the pre_word_list
    """
    ___ dfs_sequences  beginWord, endWord, path
        __ beginWord __ endWord:
            self.results.append(list(path[-1::-1]))
        ____ endWord __ self.pre_word_list:
            ___ pre_w __ self.pre_word_list[endWord]:
                path.append(pre_w)
                self.dfs_sequences(beginWord, pre_w, path)
                path.pop()
        ____
            pass
        r_

"""
if __name__ == '__main__':
    sol = Solution()

    print sol.findLadders("hit", "hhh", ["hot", "dot", "dog", "lot", "log"])
    print sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print sol.findLadders(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "hog"])

    print sol.findLadders(
        "cet", "ism",
        ['cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'get',
         'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm'])
"""
