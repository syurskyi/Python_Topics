____ copy _______ deepcopy
class Matrix(object):

    ___ __init__(self, values):
        self.values = values
    


    @property
    ___ nrows(self):
        r.. l..(self.values)


    @property
    ___ ncols(self):
        r.. l..(self.values[0])

    ___ __matmul__(self,other):

        
        rows_1,cols_1 = l..(self.values),l..(self.values[0])
        rows_2,cols_2 = l..(other.values),l..(other.values[0])


        result_rows,result_cols = rows_1,cols_2


        result_matrix = [[N.. ___ _ __ r..(result_cols)] ___ _ __ r..(result_rows)]



        ___ row __ r..(result_rows):
            ___ col __ r..(result_cols):
                value = 0
                ___ c __ r..(cols_1):
                    value += self.values[row][c] * other.values[c][col]

                result_matrix[row][col] = value
        

        r.. Matrix(result_matrix)

    ___ __imatmul__(self,other):


        result = self @ other

        self.values = deepcopy(result.values)


        r.. self

    
    ___ __rmatmul__(self,other):

        r.. self  @ other















    ___ __repr__(self):
        r.. f'<Matrix values="{self.values}">'


