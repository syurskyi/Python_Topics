c_ Solution:
    ___ escapeGhosts  ghosts, target
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        R, C target
        pacman_dist a..(R) + a..(C)  # (R - 0) + (C - 0)

        ___ x, y __ ghosts:
            ghost_dist a..(R - x) + a..(C - y)
            __ ghost_dist <_ pacman_dist:
                r.. F..

        r.. T..
