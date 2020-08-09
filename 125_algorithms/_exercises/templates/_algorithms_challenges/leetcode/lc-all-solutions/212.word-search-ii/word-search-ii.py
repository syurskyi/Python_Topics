class TrieNode:
  ___ __init__(self, char
    self.neighbours = {}
    self.isWord = False


class Trie:
  ___ __init__(self
    self.root = TrieNode("-")

  ___ addWord(self, word
    root = self.root
    ___ i in range(0, le.(word)):
      c = word[i]
      __ c in root.neighbours:
        root = root.neighbours[c]
      ____
        newnode = TrieNode(c)
        root.neighbours[c] = newnode
        root = root.neighbours[c]
    root.isWord = True


class Solution:
  # @param board, a list of lists of 1 length string
  # @param words: A list of string
  # @return: A list of string
  ___ findWords(self, board, words
    # write your code here
    trie = Trie()
    res = []
    visited = [[0] * le.(board[0]) ___ i in range(0, le.(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ dfs(i, j, board, visited, res, root, path
      __ not root:
        r_

      __ root.isWord:
        res.append(path)

      ___ direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        __ 0 <= ni < le.(board) and 0 <= nj < le.(board[0]
          c = board[ni][nj]
          __ visited[ni][nj] __ 0:
            visited[ni][nj] = 1
            dfs(ni, nj, board, visited, res, root.neighbours.get(c, None), path + c)
            visited[ni][nj] = 0

    ___ word in words:
      trie.addWord(word)
    root = trie.root
    ___ i in range(0, le.(board)):
      ___ j in range(0, le.(board[0])):
        c = board[i][j]
        visited[i][j] = 1
        dfs(i, j, board, visited, res, root.neighbours.get(c, None), c)
        visited[i][j] = 0
    r_ list(set(res))
