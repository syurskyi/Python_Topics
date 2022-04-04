"""
Given two words (beginWord and endWord), and a dictionary, find the length of
shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

c_ Solution(o..
    ___ ladderLength  beginWord, endWord, wordDict
        """
        :type beginWord: str
        :type endWord: str
        :type wordDict: Set[str]
        :rtype: int
        """
        queue    # list
        queue.a..((beginWord, 0
        letters = map(chr, r..(o..('a'), o..('z') + 1
        word_dict = wordDict
        # Remove words that are same as beginWord
        ___ word __ s..(wordDict
            __ beginWord __ word:
                wordDict.remove(beginWord)
        wordDict.add(endWord)
        w.... queue:
            cur = queue.pop(0)
            __ cur[0] __ endWord:
                r.. cur[1] + 1
            ___ word __ get_adjacent(cur[0]
                wordDict.remove(word)  # Mark as visited
                queue.a..((word, cur[1] + 1
        r.. 0

    ___ get_adjacent  word1
        res    # list
        ___ i, e __ e..(word1
            ___ letter __ letters:
                word = word1[:i] + letter + word1[i + 1:]
                __ word __ word_dict:
                    res.a..(word)
        r.. res


s = Solution()
print s.ladderLength("hit", "dow", s..(["hot", "dot", "dog", "lot", "log"]
print s.ladderLength("hit", "cog", s..(["hot", "dot", "dog", "lot", "log"]
print s.ladderLength("hit", "cog", s..(["aos", "dis", "dog", "lot", "log"]
