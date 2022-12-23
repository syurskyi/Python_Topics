c_ Solution o..
    ___ maximalRectangle  matrix
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/6650/share-my-dp-solution/2
        __ matrix is N.. or l.. matrix) __ 0:
            r_ 0
        ls_row, ls_col = l.. matrix), l.. matrix[0])
        left, right, height = [0] * ls_col, [ls_col] * ls_col, [0] * ls_col
        maxA = 0
        ___ i __ r.. ls_row
            curr_left, curr_right = 0, ls_col
            ___ j __ r.. ls_col
                __ matrix[i][j] __ '1':
                    height[j] += 1
                ____
                    height[j] = 0
            ___ j __ r.. ls_col
                __ matrix[i][j] __ '1':
                    left[j] = m..(left[j], curr_left)
                ____
                    left[j], curr_left = 0, j + 1
            ___ j __ r.. ls_col - 1, -1, -1
                __ matrix[i][j] __ '1':
                    right[j] = m.. right[j], curr_right)
                ____
                    right[j], curr_right = ls_col, j
            ___ j __ r.. ls_col
                maxA = m..(maxA, (right[j] - left[j]) * height[j])
        r_ maxA



