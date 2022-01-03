_______ string
____ collections _______ deque


c_ Solution(object):
  ___ ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """

    ___ getNbrs(src, dest, wordList):
      res    # list
      ___ c __ string.ascii_lowercase:
        ___ i __ r..(0, l..(src)):
          newWord = src[:i] + c + src[i + 1:]
          __ newWord __ src:
            continue
          __ newWord __ wordList o. newWord __ dest:
            y.. newWord

    queue = deque([beginWord])
    length = 0
    w.... queue:
      length += 1
      ___ k __ r..(0, l..(queue)):
        top = queue.popleft()
        ___ nbr __ getNbrs(top, endWord, wordList):
          wordList.remove(nbr)
          __ nbr __ endWord:
            r.. length + 1
          queue.a..(nbr)
    r.. 0
