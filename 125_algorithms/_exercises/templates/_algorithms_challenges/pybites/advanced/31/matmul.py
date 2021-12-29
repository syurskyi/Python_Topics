from copy import deepcopy
class Matrix(object):

    ___ __init__(self, values):
        self.values = values
    


    @property
    ___ nrows(self):
        return len(self.values)


    @property
    ___ ncols(self):
        return len(self.values[0])

    ___ __matmul__(self,other):

        
        rows_1,cols_1 = len(self.values),len(self.values[0])
        rows_2,cols_2 = len(other.values),len(other.values[0])


        result_rows,result_cols = rows_1,cols_2


        result_matrix = [[None for _ in range(result_cols)] for _ in range(result_rows)]



        for row in range(result_rows):
            for col in range(result_cols):
                value = 0
                for c in range(cols_1):
                    value += self.values[row][c] * other.values[c][col]

                result_matrix[row][col] = value
        

        return Matrix(result_matrix)

    ___ __imatmul__(self,other):


        result = self @ other

        self.values = deepcopy(result.values)


        return self

    
    ___ __rmatmul__(self,other):

        return self  @ other















    ___ __repr__(self):
        return f'<Matrix values="{self.values}">'


