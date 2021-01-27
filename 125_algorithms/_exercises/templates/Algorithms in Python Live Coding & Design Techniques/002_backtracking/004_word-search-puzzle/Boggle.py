my_dict = {'RAY', 'APPLE', 'FAKE', 'BOOKS'}
m = 4
n = 4


___ find_words(boggle, visited, i, j, word
    visited[i][j] = 1
    word = ''.j..([word, boggle[i][j]])

    __ word __ my_dict:
        print(word)

    ___ row __ ra__(i-1, i+2
        ___ col __ ra__(j-1, j+2
            __ is_valid(row, col, visited
                find_words(boggle, visited, row, col, word)

    visited[i][j] = 0


___ is_valid(row, col, visited
    __ 0 <= row < m a__ 0 <= col < n a__ visited[row][col] __ 0:
        r_ T..
    r_ F..


boggle =[['T', 'Y', 'R', 'S'],
         ['N', 'U', 'A', 'K'],
         ['Z', 'F', 'E', 'O'],
         ['A', 'C', 'B','O']]

visited = [[0 ___ j __ ra__(n)] ___ i __ ra__(m)]

___ i __ ra__(m
    ___ j __ ra__(n
        find_words(boggle, visited, i, j, '')

