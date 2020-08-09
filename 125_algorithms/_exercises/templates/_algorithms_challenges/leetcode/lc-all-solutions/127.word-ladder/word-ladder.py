______ string
from collections ______ deque


class Solution(object
  ___ ladderLength(self, beginWord, endWord, wordList
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """

    ___ getNbrs(src, dest, wordList
      res = []
      for c in string.ascii_lowercase:
        for i in range(0, le.(src)):
          newWord = src[:i] + c + src[i + 1:]
          __ newWord __ src:
            continue
          __ newWord in wordList or newWord __ dest:
            yield newWord

    queue = deque([beginWord])
    length = 0
    w___ queue:
      length += 1
      for k in range(0, le.(queue)):
        top = queue.popleft()
        for nbr in getNbrs(top, endWord, wordList
          wordList.remove(nbr)
          __ nbr __ endWord:
            r_ length + 1
          queue.append(nbr)
    r_ 0
