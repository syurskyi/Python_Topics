class Solution:
    """
    @param: S: An array of char
    @param: x: An integer
    @return: nothing
    """
    ___ rotateString(self, S, x):
        __ n.. S o. n.. x:
            r.. S

        n = l..(S)
        x %= n
        self.reverse(S, 0, n - x - 1)
        self.reverse(S, n - x, n - 1)
        self.reverse(S, 0, n - 1)

    ___ reverse(self, S, start, end):
        while start < end:
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1
