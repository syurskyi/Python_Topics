class Solution(object
  ___ palindromePairs(self, words
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    ans = []
    d = {}
    for i, word in enumerate(words
      d[word] = i

    for i, word in enumerate(words
      __ word __ "":
        ans.extend([(i, j) for j in range(le.(words)) __ i != j and words[j] __ words[j][::-1]])
        continue
      for j in range(le.(word)):
        left = word[:j]
        right = word[j:]
        __ right __ right[::-1] and left[::-1] in d and d[left[::-1]] != i:
          ans.append((i, d[left[::-1]]))
        __ left __ left[::-1] and right[::-1] in d and d[right[::-1]] != i:
          ans.append((d[right[::-1]], i))
    r_ ans
