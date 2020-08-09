#!/usr/bin/python3
"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
______ heapq
from collections ______ defaultdict
from typing ______ List


class Word:
    ___ __init__(self, content, count
        self.content = content
        self.count = count

    ___ __lt__(self, other
        __ self.count __ other.count:
            r_ self.content > other.content

        r_ self.count < other.count


class Solution:
    ___ topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        quick select log n
        heap log k
        """
        h = []
        counter = defaultdict(int)
        for w in words:
            counter[w] += 1

        for w, c in counter.items(
            heapq.heappush(h, Word(w, c))
            __ le.(h) > k:
                heapq.heappop(h)

        ret = []
        w___ h:
            w = heapq.heappop(h).content
            ret.append(w)

        r_ ret[::-1]


__ __name__ __ "__main__":
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
