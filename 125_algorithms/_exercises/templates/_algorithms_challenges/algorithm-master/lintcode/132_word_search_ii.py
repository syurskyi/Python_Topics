class Solution:
    ___ __init__(self):
        self.root = self.new_node()
        self.row_vector = [1, -1, 0, 0]
        self.col_vector = [0, 0, 1, -1]

    ___ new_node(self):
        return {
            'end_of': '',
            'children': {}
        }

    ___ put(self, parent, string):
        __ not string:
            return
        for char in string:
            __ char in parent['children']:
                parent = parent['children'][char]
            else:
                parent['children'][char] = self.new_node()
                parent = parent['children'][char]
        parent['end_of'] = string

    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    ___ wordSearchII(self, board, words):
        __ not words or len(words) < 1 \
                or not board or len(board) < 1 \
                or len(board[0]) < 1:
            return []
        self.m, self.n = len(board), len(board[0])
        self.board = board
        for word in words:
            self.put(self.root, word)
        result = {}
        for row in range(self.m):
            for col in range(self.n):
                __ board[row][col] in self.root['children']:
                    self.find(row, col, self.root, result)
        return result.keys()

    ___ find(self, x, y, parent, result):
        char = self.board[x][y]
        __ char not in parent['children']:
            return
        parent = parent['children'][char]
        __ parent['end_of']:
            result[parent['end_of']] = 1
            parent['end_of'] = ''

        # To avoid returning along the original path, just simply set the last visited cell to `'#'`
        self.board[x][y] = '#'
        for d in range(4):
            _x = x + self.row_vector[d]
            _y = y + self.col_vector[d]
            __ 0 <= _x < self.m \
                    and 0 <= _y < self.n \
                    and self.board[_x][_y] in parent['children']:
                self.find(_x, _y, parent, result)
        self.board[x][y] = char
