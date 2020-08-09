class Solution:
    ___ trap(self, height: List[int]) -> int:
        n = le.(height)
        __(n __ 0
            r_ 0

        left = [0]*n
        right = [0] * n

        ans = 0

        left[0] = height[0]

        for i in range(1, n
            left[i] = max(left[i-1], height[i])

        right[n-1] = height[n-1]

        for i in range(n-2, -1, -1
            right[i] = max(right[i+1], height[i])

        for i in range(0, n
            ans += min(left[i], right[i])-height[i]

        r_ ans
