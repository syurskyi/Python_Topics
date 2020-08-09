c_ Solution:
    ___ trap(, height: L.. in.) -> int:
        n _ le.(height)
        __(n __ 0
            r_ 0

        left _ [0]*n
        right _ [0] * n

        ans _ 0

        left[0] _ height[0]

        ___ i __ ra..(1, n
            left[i] _ ma.(left[i-1], height[i])

        right[n-1] _ height[n-1]

        ___ i __ ra..(n-2, -1, -1
            right[i] _ ma.(right[i+1], height[i])

        ___ i __ ra..(0, n
            ans +_ min(left[i], right[i])-height[i]

        r_ ans
