"""
Test Case:

"a"
"a"
["b"]
=> should check again words in queue
"""


class Solution:
    ___ ladderLength(self, s, e, D):
        """
        :type s: str
        :type e: str
        :type D: List[str]
        :rtype: int
        """
        __ (not s or not e or
            len(s) != len(e) or not D):
            return 0
        __ s == e:
            return 1

        __ s not in D:
            D.append(s)
        __ e not in D:
            D.append(e)

        n = len(s)
        next_words = [None] * n
        for i in range(n):
            next_words[i] = _words = {}
            for word in D:
                key = word[:i] + word[i + 1:]
                __ key not in _words:
                    _words[key] = set()
                _words[key].add(word)

        queue = [e]
        distance = {e: 1}
        for word in queue:
            for _word in self.get_next_word(word, next_words):
                __ _word in distance:
                    continue
                distance[_word] = distance[word] + 1
                __ _word == s:
                    return distance[_word]
                queue.append(_word)

        return 0

    ___ get_next_word(self, word, next_words):
        for i in range(len(word)):
            key = word[:i] + word[i + 1:]
            __ key not in next_words[i]:
                continue
            for _word in next_words[i][key]:
                __ _word == word:
                    continue
                yield _word
