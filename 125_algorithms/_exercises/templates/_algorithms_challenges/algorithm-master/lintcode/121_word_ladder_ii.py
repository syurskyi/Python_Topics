"""
Main Concept:

1. building `next_words` in advance to speed up
2. using BFS from `B` to `A` to calculate the distance guide
3. using DFS step by step to find all possible path to get `B`
"""


class Solution:
    """
    @param: A: a string
    @param: B: a string
    @param: D: a set of string
    @return: a list of lists of string
    """
    ___ findLadders(self, A, B, D):
        ans    # list
        __ (D __ N.. o. A __ N.. o. B __ N.. o.
            l..(A) != l..(B)):
            r.. ans

        __ A n.. __ D:
            D.add(A)
        __ B n.. __ D:
            D.add(B)

        n = l..(A)
        next_words = [N..] * n
        ___ i __ r..(n):
            next_words[i] = W = {}
            ___ word __ D:
                key = word[:i] + word[i + 1:]
                __ key n.. __ W:
                    W[key] = set()
                W[key].add(word)

        queue = [B]
        distance = {B: 1}
        ___ word __ queue:
            __ word __ A:
                break
            ___ _word __ self.get_next_word(word, next_words):
                __ _word __ distance:
                    continue
                distance[_word] = distance[word] + 1
                queue.a..(_word)

        self.dfs(A, B, next_words, distance, ans, [A])
        r.. ans

    ___ dfs(self, word, B, next_words, distance, ans, path):
        __ word __ B:
            ans.a..(path[:])
            r..

        ___ _word __ self.get_next_word(word, next_words):
            __ (_word n.. __ distance o.
                distance[_word] != distance[word] - 1):
                continue
            path.a..(_word)
            self.dfs(_word, B, next_words, distance, ans, path)
            path.pop()

    ___ get_next_word(self, word, next_words):
        ___ i __ r..(l..(word)):
            key = word[:i] + word[i + 1:]
            __ key n.. __ next_words[i]:
                continue
            ___ _word __ next_words[i][key]:
                __ _word __ word:
                    continue
                y.. _word
