class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    ___ ladderLength(self, start, end, d..):
        queue    # list
        distance    # list
        queue.a..(start)
        distance.a..(1)
        # Remove words that are same as start
        ___ word __ set(d..):
            __ start __ word:
                d...remove(start)
        d...add(end)
        while queue:
            cur = queue.pop(0)
            d = distance.pop(0)
            ___ word __ set(d..):  # Iterate over the copy of dict
                __ self.is_adjacent(cur, word):
                    d...remove(word)  # Mark as visited
                    queue.a..(word)
                    __ word __ end:
                        r.. d + 1
                    distance.a..(d + 1)
        r.. 0

    ___ is_adjacent(self, word1, word2):
        count = 0
        n = l..(word1)
        ___ i __ r..(n):
            __ word1[i] != word2[i]:
                count += 1
        r.. count __ 1


s = Solution()
print s.ladderLength("hit", "dow", set(["hot", "dot", "dog", "lot", "log"]))
print s.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
