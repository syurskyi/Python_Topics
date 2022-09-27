c_ Solution o..
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     try:
    #         ls_row, ls_col = len(matrix), len(matrix[0])
    #     except:
    #         return False
    #     begin, end = 0, ls_row - 1
    #     while begin <= end:
    #         mid = (begin +  end) / 2
    #         res = self.search_row(matrix, mid, target)
    #         if res == 0:
    #             return True
    #         elif res < 0:
    #             end = mid - 1
    #         else:
    #             begin = mid + 1
    #     return False
    #
    #
    # def search_row(self, matrix, row, target):
    #     if target < matrix[row][0]:
    #         return -1
    #     elif target > matrix[row][-1]:
    #         return 1
    #     begin, end = 0, len(matrix[row]) - 1
    #     while begin <= end:
    #         mid = (begin + end) / 2
    #         if matrix[row][mid] == target:
    #             return 0
    #         elif matrix[row][mid] < target:
    #             begin = mid + 1
    #         else:
    #             end = mid - 1
    #     return 1


    ___ searchMatrix  matrix, target):
        # binary search
        try:
            ls_row, ls_col = l.. matrix), l.. matrix[0])
        except:
            r_ F..
        __ target < matrix[0][0] or target > matrix[-1][-1]:
            r_ F..
        begin, end = 0, ls_row * ls_col - 1
        w.. begin <= end:
            mid = (begin + end) / 2
            row, col = mid / ls_col, mid % ls_col
            __ matrix[row][col] __ target:
                r_ T..
            ____ matrix[row][col] > target:
                end = mid - 1
            ____
                begin = mid + 1
        r_ F..


