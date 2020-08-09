class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    ___ ladderLength(self, start, end, dict
        queue = []
        distance = []
        queue.append(start)
        distance.append(1)
        # Remove words that are same as start
        for word in set(dict
            __ start __ word:
                dict.remove(start)
        dict.add(end)
        w___ queue:
            cur = queue.pop(0)
            d = distance.pop(0)
            for word in set(dict  # Iterate over the copy of dict
                __ self.is_adjacent(cur, word
                    dict.remove(word)  # Mark as visited
                    queue.append(word)
                    __ word __ end:
                        r_ d + 1
                    distance.append(d + 1)
        r_ 0

    ___ is_adjacent(self, word1, word2
        count = 0
        n = le.(word1)
        for i in range(n
            __ word1[i] != word2[i]:
                count += 1
        r_ count __ 1


s = Solution()
print s.ladderLength("hit", "dow", set(["hot", "dot", "dog", "lot", "log"]))
print s.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
