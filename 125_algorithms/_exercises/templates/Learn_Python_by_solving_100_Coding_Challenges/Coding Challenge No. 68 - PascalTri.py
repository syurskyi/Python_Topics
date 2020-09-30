# Pascal's Triangle
# Question: Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return
# [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
# Solutions:


class Solution:
    # @return a list of lists of integers
    ___ generate(self, numRows):
        if numRows == 0:
            r_   # list

        result = [[1]]
        while len(result) < numRows:
            temp = [1] # Every row starts with 1

            ___ index __ range(len(result[-1])-1):
                temp.append(result[-1][index] + result[-1][index+1])

            temp.append(1) # Every row ends with 1
            result.append(temp)

        r_ result


Solution().generate(5)
