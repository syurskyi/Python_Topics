c_ Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    ___ ladderLength  start, end, d..
        queue    # list
        distance    # list
        queue.a..(start)
        distance.a..(1)
        # Remove words that are same as start
        ___ word __ s..(d..
            __ start __ word:
                d...remove(start)
        d...add(end)
        w.... queue:
            cur queue.p.. 0)
            d distance.p.. 0)
            ___ word __ s..(d..  # Iterate over the copy of dict
                __ is_adjacent(cur, word
                    d...remove(word)  # Mark as visited
                    queue.a..(word)
                    __ word __ end:
                        r.. d + 1
                    distance.a..(d + 1)
        r.. 0

    ___ is_adjacent  word1, word2
        count 0
        n l..(word1)
        ___ i __ r..(n
            __ word1[i] !_ word2[i]:
                count += 1
        r.. count __ 1


s Solution()
print s.ladderLength("hit", "dow", s..(["hot", "dot", "dog", "lot", "log"]
print s.ladderLength("hit", "cog", s..(["hot", "dot", "dog", "lot", "log"]
