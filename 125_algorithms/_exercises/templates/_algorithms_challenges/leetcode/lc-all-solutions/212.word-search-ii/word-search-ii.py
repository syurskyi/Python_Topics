class TrieNode:
  ___ __init__(self, char):
    self.neighbours = {}
    self.isWord = False


class Trie:
  ___ __init__(self):
    self.root = TrieNode("-")

  ___ addWord(self, word):
    root = self.root
    ___ i __ r..(0, l..(word)):
      c = word[i]
      __ c __ root.neighbours:
        root = root.neighbours[c]
      ____:
        newnode = TrieNode(c)
        root.neighbours[c] = newnode
        root = root.neighbours[c]
    root.isWord = True


class Solution:
  # @param board, a list of lists of 1 length string
  # @param words: A list of string
  # @return: A list of string
  ___ findWords(self, board, words):
    # write your code here
    trie = Trie()
    res    # list
    visited = [[0] * l..(board[0]) ___ i __ r..(0, l..(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ dfs(i, j, board, visited, res, root, path):
      __ n.. root:
        r..

      __ root.isWord:
        res.a..(path)

      ___ direction __ directions:
        ni, nj = i + direction[0], j + direction[1]
        __ 0 <= ni < l..(board) a.. 0 <= nj < l..(board[0]):
          c = board[ni][nj]
          __ visited[ni][nj] __ 0:
            visited[ni][nj] = 1
            dfs(ni, nj, board, visited, res, root.neighbours.get(c, N..), path + c)
            visited[ni][nj] = 0

    ___ word __ words:
      trie.addWord(word)
    root = trie.root
    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        c = board[i][j]
        visited[i][j] = 1
        dfs(i, j, board, visited, res, root.neighbours.get(c, N..), c)
        visited[i][j] = 0
    r.. l..(set(res))
