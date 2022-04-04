c_ Solution:
    # @return an integer
    ___ minDistance  word1, word2
        n = l..(word1)
        m = l..(word2)
        d = [[0 ___ j __ r..(m + 1)] ___ i __ r..(n + 1)]
        ___ i __ r..(n + 1
            d[i][0] = i
        ___ j __ r..(m + 1
            d[0][j] = j
        ___ i __ r..(1, n + 1
            ___ j __ r..(1, m + 1
                __ word1[i - 1] __ word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                ____
                    op = m..(d[i - 1][j - 1],  # Substitute
                             d[i - 1][j],  # Insert
                             d[i][j - 1])  # Delete
                    d[i][j] = op + 1
        r.. d[n][m]
