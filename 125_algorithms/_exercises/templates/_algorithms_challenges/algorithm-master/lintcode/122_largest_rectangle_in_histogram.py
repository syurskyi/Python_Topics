"""
REF: https://aaronice.gitbooks.io/lintcode/content/data_structure/largest_rectangle_in_histogram.html
"""


"""
Brute Force: TLE
"""
c_ Solution:
    ___ largestRectangleArea  H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ n.. H:
            r.. ans

        n = l..(H)
        L = [0] * n  # lowest height

        ___ left __ r..(n):
            ___ right __ r..(left, n):
                L[right] = H[right]

                __ right > left a.. L[right - 1] < H[right]:
                    L[right] = L[right - 1]

                area = L[right] * (right - left + 1)
                __ area > ans:
                    ans = area

        r.. ans


"""
Brute Force with Pruning
"""
c_ Solution:
    ___ largestRectangleArea  H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ n.. H:
            r.. ans

        n = l..(H)

        ___ right __ r..(l..(H)):
            __ right < n - 1 a.. H[right] <= H[right + 1]:
                _____
            Hmin = H[right]
            ___ left __ r..(right, -1, -1):
                __ H[left] < Hmin:
                    Hmin = H[left]

                area = Hmin * (right - left + 1)
                __ area > ans:
                    ans = area

        r.. ans


"""
Mono-stack
"""
c_ Solution:
    ___ largestRectangleArea  H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ n.. H:
            r.. ans

        H.a..(0)
        stack    # list

        ___ right __ r..(l..(H)):
            w.... stack a.. H[stack[-1]] >= H[right]:
                height = H[stack.pop()]
                left = stack[-1] __ stack ____ -1
                area = height * (right - left - 1)
                __ area > ans:
                    ans = area
            stack.a..(right)

        r.. ans
