import string
from collections import deque


class Solution(object):
  ___ ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """

    ___ getNbrs(src, dest, wordList):
      res = []
      for c in string.ascii_lowercase:
        for i in range(0, len(src)):
          newWord = src[:i] + c + src[i + 1:]
          __ newWord == src:
            continue
          __ newWord in wordList or newWord == dest:
            yield newWord

    queue = deque([beginWord])
    length = 0
    while queue:
      length += 1
      for k in range(0, len(queue)):
        top = queue.popleft()
        for nbr in getNbrs(top, endWord, wordList):
          wordList.remove(nbr)
          __ nbr == endWord:
            return length + 1
          queue.append(nbr)
    return 0
