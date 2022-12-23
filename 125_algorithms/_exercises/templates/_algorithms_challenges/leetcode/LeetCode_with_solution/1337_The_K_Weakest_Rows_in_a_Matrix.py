c_ Solution o..
    ___ kWeakestRows  mat, k
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res =    # list
        num_row = l.. mat)
        num_col = l.. mat[0])
        col = 0
        flag = 1
        w.. col < num_col a.. flag:
            ___ i __ r.. num_row
                __ i __ res:
                    c_
                # Add first row with 0 into res
                __ mat[i][col] __ 0:
                    res.a.. i)
                __ l.. res) __ k:
                    flag = 0
                    ______
            col += 1
        __ l.. res) __ k:
            r_ res
        # if res less than k
        ___ i __ r.. num_row
            __ i __ res:
                c_
            res.a.. i)
            __ l.. res) __ k:
                ______
        r_ res