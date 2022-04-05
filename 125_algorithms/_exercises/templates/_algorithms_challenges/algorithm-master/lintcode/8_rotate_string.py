c_ Solution:
    """
    @param: S: An array of char
    @param: x: An integer
    @return: nothing
    """
    ___ rotateString  S, x
        __ n.. S o. n.. x:
            r.. S

        n = l..(S)
        x %= n
        reverse(S, 0, n - x - 1)
        reverse(S, n - x, n - 1)
        reverse(S, 0, n - 1)

    ___ reverse  S, start, end
        w.... start < end:
            S[start], S[end] = S[end], S[start]
            start += 1
            end -_ 1
