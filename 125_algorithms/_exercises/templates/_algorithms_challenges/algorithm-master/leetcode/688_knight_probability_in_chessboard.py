_______ c..


c_ Solution:
    """
    DP:
    1. init the first pos as 1
    2. keep simulate the process and divide the probability
    3. sum the values
    """
    ___ knightProbability  n, k, r, c
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp c...d.. i..
        dp[r, c] 1.0

        ___ _ __ r..(k
            nxt c...d.. i..

            ___ x __ r..(n
                ___ y __ r..(n
                    ___ dx, dy __ (
                        (-1, -2),
                        ( 1, -2),
                        (-2, -1),
                        ( 2, -1),
                        (-2,  1),
                        ( 2,  1),
                        (-1,  2),
                        ( 1,  2),

                        _x x + dx
                        _y y + dy

                        __ n.. (0 <_ _x < n a.. 0 <_ _y < n
                            _____

                        nxt[_x, _y] += dp[x, y] / 8.0

            dp nxt

        r.. s..(dp.values


c_ Solution:
    """
    BFS: TLE
    """
    ___ knightProbability  n, k, r, c
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        __ n __ 1 a.. k __ 0:
            r.. 1.0

        queue, _queue [(r, c)],    # list
        total 8 ** k
        valid 0

        w.... queue a.. k:
            k -_ 1

            ___ x, y __ queue:
                ___ dx, dy __ (
                    (-1, -2),
                    ( 1, -2),
                    (-2, -1),
                    ( 2, -1),
                    (-2,  1),
                    ( 2,  1),
                    (-1,  2),
                    ( 1,  2),

                    _x x + dx
                    _y y + dy

                    __ n.. (0 <_ _x < n a.. 0 <_ _y < n
                        _____

                    __ k __ 0:
                        valid += 1

                    __ k > 0
                        _queue.a..((_x, _y

            queue, _queue _queue,    # list

        r.. valid / total
