class Solution:
    ___ escapeGhosts(self, ghosts, target
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        R, C = target
        pacman_dist = abs(R) + abs(C)  # (R - 0) + (C - 0)

        for x, y in ghosts:
            ghost_dist = abs(R - x) + abs(C - y)
            __ ghost_dist <= pacman_dist:
                r_ False

        r_ True
