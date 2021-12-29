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
        __ (n.. s o. n.. e o.
            l..(s) != l..(e) o. n.. D):
            r.. 0
        __ s __ e:
            r.. 1

        __ s n.. __ D:
            D.a..(s)
        __ e n.. __ D:
            D.a..(e)

        n = l..(s)
        next_words = [N..] * n
        ___ i __ r..(n):
            next_words[i] = _words = {}
            ___ word __ D:
                key = word[:i] + word[i + 1:]
                __ key n.. __ _words:
                    _words[key] = set()
                _words[key].add(word)

        queue = [e]
        distance = {e: 1}
        ___ word __ queue:
            ___ _word __ self.get_next_word(word, next_words):
                __ _word __ distance:
                    continue
                distance[_word] = distance[word] + 1
                __ _word __ s:
                    r.. distance[_word]
                queue.a..(_word)

        r.. 0

    ___ get_next_word(self, word, next_words):
        ___ i __ r..(l..(word)):
            key = word[:i] + word[i + 1:]
            __ key n.. __ next_words[i]:
                continue
            ___ _word __ next_words[i][key]:
                __ _word __ word:
                    continue
                yield _word
