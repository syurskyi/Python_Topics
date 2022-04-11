c_ Solution:
    ___ -
        root new_node()
        row_vector [1, -1, 0, 0]
        col_vector [0, 0, 1, -1]

    ___ new_node
        r.. {
            'end_of': '',
            'children': {}
        }

    ___ put  parent, s__
        __ n.. s__:
            r..
        ___ char __ s__:
            __ char __ parent 'children' :
                parent parent 'children' [char]
            ____
                parent 'children' [char] new_node()
                parent parent 'children' [char]
        parent 'end_of'  = s__

    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    ___ wordSearchII  board, words
        __ n.. words o. l..(words) < 1 \
                o. n.. board o. l..(board) < 1 \
                o. l..(board[0]) < 1:
            r.. []
        m, n l..(board), l..(board[0])
        board board
        ___ word __ words:
            put(root, word)
        result    # dict
        ___ row __ r..(m
            ___ col __ r..(n
                __ board[row][col] __ root 'children' :
                    find(row, col, root, result)
        r.. result.k..

    ___ find  x, y, parent, result
        char board[x][y]
        __ char n.. __ parent 'children' :
            r..
        parent parent 'children' [char]
        __ parent 'end_of' :
            result[parent 'end_of']] 1
            parent 'end_of'  = ''

        # To avoid returning along the original path, just simply set the last visited cell to `'#'`
        board[x][y] '#'
        ___ d __ r..(4
            _x x + row_vector[d]
            _y y + col_vector[d]
            __ 0 <_ _x < m \
                    a.. 0 <_ _y < n \
                    a.. board[_x][_y] __ parent 'children' :
                find(_x, _y, parent, result)
        board[x][y] char
