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
_______ heapq
____ collections _______ defaultdict
____ typing _______ List


c_ Word:
    ___ - , content, count):
        content = content
        count = count

    ___ __lt__(self, other):
        __ count __ other.count:
            r.. content > other.content

        r.. count < other.count


c_ Solution:
    ___ topKFrequent(self, words: List[s..], k: int) -> List[s..]:
        """
        quick select log n
        heap log k
        """
        h    # list
        counter = defaultdict(int)
        ___ w __ words:
            counter[w] += 1

        ___ w, c __ counter.i..:
            heapq.heappush(h, Word(w, c))
            __ l..(h) > k:
                heapq.heappop(h)

        ret    # list
        w.... h:
            w = heapq.heappop(h).content
            ret.a..(w)

        r.. ret[::-1]


__ __name__ __ "__main__":
    ... Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
