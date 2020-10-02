# Pascal's Triangle
# Question: Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return
# [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
# Solutions:


c_ Solution:
    # @return a list of lists of integers
    ___ generate , numRows:
        __ numRows __ 0:
            r_   # list

        result _ [[1]]
        w___ le. result < numRows:
            temp _ [1] # Every row starts with 1

            ___ index __ ra.. le. result[-1]-1:
                temp.ap.. result[-1][index] + result[-1][index+1]

            temp.ap.. 1 # Every row ends with 1
            result.ap.. temp

        r_ result


Solution .generate 5
