c_ TrieNode:
    ___ - ):
        children    # dict
        end_of = N..


c_ Solution:
    ___ boggleGame  board, words):
        """
        :type board: list[list[str]]
        :type words: list[str]
        :rtype: int
        """
        ans = 0

        __ n.. board o. n.. board[0]:
            r.. ans


        root = TrieNode()

        ___ word __ words:
            put(root, word)


        m, n = l..(board), l..(board[0])
        visited = set()

        ___ x __ r..(m):
            ___ y __ r..(n):
                dfs(board, x, y, root, visited, 0)


        r.. ans

    ___ dfs  board, i, j, root, visited, cnt):
        m, n = l..(board), l..(board[0])

        ___ x __ r..(i, m):
            ___ y __ r..(j, n):
                next_words    # list
                find_next_words(board, x, y, visited, cnt, root, next_words, [])

                ___ pos __ next_words:
                    ___ p __ pos:
                        visited.add(p)

                    dfs(board, x, y, root, visited, cnt + 1)

                    ___ p __ pos:
                        visited.discard(p)

            j = 0

    ___ find_next_words  board, x, y, visited, cnt, node, next_words, path):
        __ (x, y) __ visited o. board[x][y] n.. __ node.children:
            r..

        m, n = l..(board), l..(board[0])
        node = node.children[board[x][y]]

        path.a..((x, y))
        visited.add((x, y))

        __ node.end_of __ n.. N..
            next_words.a..(path | )
            ans = m..(ans, cnt + 1)
        ____:
            ___ dx, dy __ (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),
            ):
                _x = x + dx
                _y = y + dy

                __ n.. (0 <= _x < m a.. 0 <= _y < n):
                    _____

                find_next_words(board, _x, _y, visited, cnt, node, next_words, path)

        path.pop()
        visited.discard((x, y))

    ___ put  root, word):
        node = root

        ___ c __ word:
            __ c n.. __ node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word
