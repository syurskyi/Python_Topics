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
        __ (D pa__ None or A pa__ None or B pa__ None or
            le.(A) != le.(B)):
            r_ ans

        __ A not in D:
            D.add(A)
        __ B not in D:
            D.add(B)

        n = le.(A)
        next_words = [None] * n
        ___ i in range(n
            next_words[i] = W = {}
            ___ word in D:
                key = word[:i] + word[i + 1:]
                __ key not in W:
                    W[key] = set()
                W[key].add(word)

        queue = [B]
        distance = {B: 1}
        ___ word in queue:
            __ word __ A:
                break
            ___ _word in self.get_next_word(word, next_words
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

        ___ _word in self.get_next_word(word, next_words
            __ (_word not in distance or
                distance[_word] != distance[word] - 1
                continue
            path.append(_word)
            self.dfs(_word, B, next_words, distance, ans, path)
            path.pop()

    ___ get_next_word(self, word, next_words
        ___ i in range(le.(word)):
            key = word[:i] + word[i + 1:]
            __ key not in next_words[i]:
                continue
            ___ _word in next_words[i][key]:
                __ _word __ word:
                    continue
                yield _word
