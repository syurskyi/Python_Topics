"""
Test Case:

"a"
"a"
["b"]
=> should check again words in queue
"""


class Solution:
    ___ ladderLength(self, s, e, D
        """
        :type s: str
        :type e: str
        :type D: List[str]
        :rtype: int
        """
        __ (not s or not e or
            le.(s) != le.(e) or not D
            r_ 0
        __ s __ e:
            r_ 1

        __ s not in D:
            D.append(s)
        __ e not in D:
            D.append(e)

        n = le.(s)
        next_words = [None] * n
        ___ i in range(n
            next_words[i] = _words = {}
            ___ word in D:
                key = word[:i] + word[i + 1:]
                __ key not in _words:
                    _words[key] = set()
                _words[key].add(word)

        queue = [e]
        distance = {e: 1}
        ___ word in queue:
            ___ _word in self.get_next_word(word, next_words
                __ _word in distance:
                    continue
                distance[_word] = distance[word] + 1
                __ _word __ s:
                    r_ distance[_word]
                queue.append(_word)

        r_ 0

    ___ get_next_word(self, word, next_words
        ___ i in range(le.(word)):
            key = word[:i] + word[i + 1:]
            __ key not in next_words[i]:
                continue
            ___ _word in next_words[i][key]:
                __ _word __ word:
                    continue
                yield _word
