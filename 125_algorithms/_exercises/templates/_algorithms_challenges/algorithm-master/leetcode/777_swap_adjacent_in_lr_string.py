class Solution:
    ___ canTransform(self, start, end
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        __ le.(start) != le.(end
            r_ False

        m, n = le.(start), le.(end)
        i = j = 0

        w___ i < m and j < n:
            w___ i < m and start[i] __ 'X':
                i += 1
            w___ j < n and end[j] __ 'X':
                j += 1

            __ i __ m and j __ n:
                r_ True
            __ i __ m or j __ n:
                r_ False

            __ start[i] != end[j]:
                r_ False
            __ start[i] __ 'L' and j > i:
                r_ False
            __ start[i] __ 'R' and i > j:
                r_ False

            i += 1
            j += 1

        r_ True
