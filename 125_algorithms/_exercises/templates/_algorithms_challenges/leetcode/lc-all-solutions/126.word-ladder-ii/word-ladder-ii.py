____ c.. _______ d..


c_ Solution(o..
  ___ findLadders  beginWord, endWord, wordlist
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """

    ___ getNbrs(src, dest, wordList
      res    # list
      ___ c __ s__.ascii_lowercase:
        ___ i __ r..(0, l..(src)):
          newWord = src[:i] + c + src[i + 1:]
          __ newWord __ src:
            _____
          __ newWord __ wordList o. newWord __ dest:
            y.. newWord

    ___ bfs(beginWord, endWord, wordList
      distance = {beginWord: 0}
      queue = d..([beginWord])
      length = 0
      w.... queue:
        length += 1
        ___ k __ r..(0, l..(queue)):
          top = queue.popleft()
          ___ nbr __ getNbrs(top, endWord, wordList
            __ nbr n.. __ distance:
              distance[nbr] = distance[top] + 1
              queue.a..(nbr)
      r.. distance

    ___ dfs(beginWord, endWord, wordList, p.., res, distance
      __ beginWord __ endWord:
        res.a..(p.. + [])
        r..

      ___ nbr __ getNbrs(beginWord, endWord, wordList
        __ distance.get(nbr, -2) + 1 __ distance[beginWord]:
          p...a..(nbr)
          dfs(nbr, endWord, wordList, p.., res, distance)
          p...pop()

    res    # list
    distance = bfs(endWord, beginWord, wordlist)
    dfs(beginWord, endWord, wordlist, [beginWord], res, distance)
    r.. res
