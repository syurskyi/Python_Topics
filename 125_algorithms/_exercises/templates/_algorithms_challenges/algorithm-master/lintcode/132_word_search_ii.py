class Solution:
    ___ __init__(self):
        self.root = self.new_node()
        self.row_vector = [1, -1, 0, 0]
        self.col_vector = [0, 0, 1, -1]

    ___ new_node(self):
        r.. {
            'end_of': '',
            'children': {}
        }

    ___ put(self, parent, string):
        __ n.. string:
            r..
        ___ char __ string:
            __ char __ parent['children']:
                parent = parent['children'][char]
            ____:
                parent['children'][char] = self.new_node()
                parent = parent['children'][char]
        parent['end_of'] = string

    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    ___ wordSearchII(self, board, words):
        __ n.. words o. l..(words) < 1 \
                o. n.. board o. l..(board) < 1 \
                o. l..(board[0]) < 1:
            r.. []
        self.m, self.n = l..(board), l..(board[0])
        self.board = board
        ___ word __ words:
            self.put(self.root, word)
        result = {}
        ___ row __ r..(self.m):
            ___ col __ r..(self.n):
                __ board[row][col] __ self.root['children']:
                    self.find(row, col, self.root, result)
        r.. result.keys()

    ___ find(self, x, y, parent, result):
        char = self.board[x][y]
        __ char n.. __ parent['children']:
            r..
        parent = parent['children'][char]
        __ parent['end_of']:
            result[parent['end_of']] = 1
            parent['end_of'] = ''

        # To avoid returning along the original path, just simply set the last visited cell to `'#'`
        self.board[x][y] = '#'
        ___ d __ r..(4):
            _x = x + self.row_vector[d]
            _y = y + self.col_vector[d]
            __ 0 <= _x < self.m \
                    and 0 <= _y < self.n \
                    and self.board[_x][_y] __ parent['children']:
                self.find(_x, _y, parent, result)
        self.board[x][y] = char
