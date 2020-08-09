class Solution:
    ___ trap(self, height: List[int]) -> int:
        n = le.(height)
        __(n __ 0
            r_ 0

        left = [0]*n
        right = [0] * n

        ans = 0

        left[0] = height[0]

        ___ i __ ra..(1, n
            left[i] = ma.(left[i-1], height[i])

        right[n-1] = height[n-1]

        ___ i __ ra..(n-2, -1, -1
            right[i] = ma.(right[i+1], height[i])

        ___ i __ ra..(0, n
            ans += min(left[i], right[i])-height[i]

        r_ ans
