____ copy _______ d..
c_ Matrix(o..):

    ___ - , values):
        values = values
    


    $
    ___ nrows
        r.. l..(values)


    $
    ___ ncols
        r.. l..(values[0])

    ___ __matmul__ other):

        
        rows_1,cols_1 = l..(values),l..(values[0])
        rows_2,cols_2 = l..(other.values),l..(other.values[0])


        result_rows,result_cols = rows_1,cols_2


        result_matrix = [[N.. ___ _ __ r..(result_cols)] ___ _ __ r..(result_rows)]



        ___ row __ r..(result_rows):
            ___ col __ r..(result_cols):
                value = 0
                ___ c __ r..(cols_1):
                    value += values[row][c] * other.values[c][col]

                result_matrix[row][col] = value
        

        r.. Matrix(result_matrix)

    ___ __imatmul__ other):


        result = self @ other

        values = d..(result.values)


        r.. self

    
    ___ __rmatmul__ other):

        r.. self  @ other















    ___  -r
        r.. f'<Matrix values="{values}">'


