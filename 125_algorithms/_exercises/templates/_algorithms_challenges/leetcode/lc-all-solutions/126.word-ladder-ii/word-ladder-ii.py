from collections ______ deque


class Solution(object
  ___ findLadders(self, beginWord, endWord, wordlist
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
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

    ___ bfs(beginWord, endWord, wordList
      distance = {beginWord: 0}
      queue = deque([beginWord])
      length = 0
      w___ queue:
        length += 1
        for k in range(0, le.(queue)):
          top = queue.popleft()
          for nbr in getNbrs(top, endWord, wordList
            __ nbr not in distance:
              distance[nbr] = distance[top] + 1
              queue.append(nbr)
      r_ distance

    ___ dfs(beginWord, endWord, wordList, path, res, distance
      __ beginWord __ endWord:
        res.append(path + [])
        r_

      for nbr in getNbrs(beginWord, endWord, wordList
        __ distance.get(nbr, -2) + 1 __ distance[beginWord]:
          path.append(nbr)
          dfs(nbr, endWord, wordList, path, res, distance)
          path.pop()

    res = []
    distance = bfs(endWord, beginWord, wordlist)
    dfs(beginWord, endWord, wordlist, [beginWord], res, distance)
    r_ res
