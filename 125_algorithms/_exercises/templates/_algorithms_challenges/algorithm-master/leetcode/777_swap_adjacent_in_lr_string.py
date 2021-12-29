class Solution:
    ___ canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        __ len(start) != len(end):
            return False

        m, n = len(start), len(end)
        i = j = 0

        while i < m and j < n:
            while i < m and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            __ i == m and j == n:
                return True
            __ i == m or j == n:
                return False

            __ start[i] != end[j]:
                return False
            __ start[i] == 'L' and j > i:
                return False
            __ start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
