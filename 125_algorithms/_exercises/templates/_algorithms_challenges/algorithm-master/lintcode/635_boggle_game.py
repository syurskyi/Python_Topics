class TrieNode:
    ___ __init__(self
        self.children = {}
        self.end_of = None


class Solution:
    ___ boggleGame(self, board, words
        """
        :type board: list[list[str]]
        :type words: list[str]
        :rtype: int
        """
        self.ans = 0

        __ not board or not board[0]:
            r_ self.ans


        root = TrieNode()

        ___ word in words:
            self.put(root, word)


        m, n = le.(board), le.(board[0])
        visited = set()

        ___ x in range(m
            ___ y in range(n
                self.dfs(board, x, y, root, visited, 0)


        r_ self.ans

    ___ dfs(self, board, i, j, root, visited, cnt
        m, n = le.(board), le.(board[0])

        ___ x in range(i, m
            ___ y in range(j, n
                next_words = []
                self.find_next_words(board, x, y, visited, cnt, root, next_words, [])

                ___ pos in next_words:
                    ___ p in pos:
                        visited.add(p)

                    self.dfs(board, x, y, root, visited, cnt + 1)

                    ___ p in pos:
                        visited.discard(p)

            j = 0

    ___ find_next_words(self, board, x, y, visited, cnt, node, next_words, path
        __ (x, y) in visited or board[x][y] not in node.children:
            r_

        m, n = le.(board), le.(board[0])
        node = node.children[board[x][y]]

        path.append((x, y))
        visited.add((x, y))

        __ node.end_of pa__ not None:
            next_words.append(path[:])
            self.ans = max(self.ans, cnt + 1)
        ____
            ___ dx, dy in (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue

                self.find_next_words(board, _x, _y, visited, cnt, node, next_words, path)

        path.p..
        visited.discard((x, y))

    ___ put(self, root, word
        node = root

        ___ c in word:
            __ c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word
