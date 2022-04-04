c_ Solution:
    ___ generate  num_rows
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        ans    # list
        __ n.. num_rows:
            r.. ans

        ans.a..([1])

        ___ i __ r..(1, num_rows
            p.. = [ans[i - 1][0]]

            ___ j __ r..(1, l..(ans[i - 1]:
                p...a..(ans[i - 1][j] + ans[i - 1][j - 1])

            p...a..(ans[i - 1][-1])
            ans.a..(p..)

        r.. ans


c_ Solution:
    ___ generate  num_rows
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        ans    # list
        __ n.. num_rows:
            r.. ans

        ans.a..([1])

        ___ i __ r..(1, num_rows
            ans.a..([
                (ans[i - 1] + [0])[j] + ([0] + ans[i - 1])[j]
                ___ j __ r..(l..(ans[i - 1]) + 1)
            ])

        r.. ans
