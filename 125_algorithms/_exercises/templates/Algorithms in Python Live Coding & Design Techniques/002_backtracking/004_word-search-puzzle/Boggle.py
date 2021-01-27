my_dict = {'RAY', 'APPLE', 'FAKE', 'BOOKS'}
m = 4
n = 4


___ find_words(boggle, visited, i, j, word
    visited[i][j] = 1
    word = ''.join([word, boggle[i][j]])

    __ word in my_dict:
        print(word)

    for row in range(i-1, i+2
        for col in range(j-1, j+2
            __ is_valid(row, col, visited
                find_words(boggle, visited, row, col, word)

    visited[i][j] = 0


___ is_valid(row, col, visited
    __ 0 <= row < m and 0 <= col < n and visited[row][col] == 0:
        return True
    return False


boggle =[['T', 'Y', 'R', 'S'],
         ['N', 'U', 'A', 'K'],
         ['Z', 'F', 'E', 'O'],
         ['A', 'C', 'B','O']]

visited = [[0 for j in range(n)] for i in range(m)]

for i in range(m
    for j in range(n
        find_words(boggle, visited, i, j, '')

