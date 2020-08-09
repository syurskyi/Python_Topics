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
    ___ findLadders(self, A, B, D
        ans = []
        __ (D is None or A is None or B is None or
            le.(A) != le.(B)):
            r_ ans

        __ A not in D:
            D.add(A)
        __ B not in D:
            D.add(B)

        n = le.(A)
        next_words = [None] * n
        for i in range(n
            next_words[i] = W = {}
            for word in D:
                key = word[:i] + word[i + 1:]
                __ key not in W:
                    W[key] = set()
                W[key].add(word)

        queue = [B]
        distance = {B: 1}
        for word in queue:
            __ word __ A:
                break
            for _word in self.get_next_word(word, next_words
                __ _word in distance:
                    continue
                distance[_word] = distance[word] + 1
                queue.append(_word)

        self.dfs(A, B, next_words, distance, ans, [A])
        r_ ans

    ___ dfs(self, word, B, next_words, distance, ans, path
        __ word __ B:
            ans.append(path[:])
            r_

        for _word in self.get_next_word(word, next_words
            __ (_word not in distance or
                distance[_word] != distance[word] - 1
                continue
            path.append(_word)
            self.dfs(_word, B, next_words, distance, ans, path)
            path.pop()

    ___ get_next_word(self, word, next_words
        for i in range(le.(word)):
            key = word[:i] + word[i + 1:]
            __ key not in next_words[i]:
                continue
            for _word in next_words[i][key]:
                __ _word __ word:
                    continue
                yield _word
