c_ Solution o..
    ___ isOneEditDistance  s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls_s, ls_t = l.. s) ,l.. t)
        # reverse to reduce conditions
        __ ls_s > ls_t:
            r_ isOneEditDistance(t, s)
        # edit distance is greater than 1
        __ ls_t - ls_s > 1:
            r_ False
        i, shift = 0, ls_t - ls_s
        # find the different position
        w.. i < ls_s and s[i] __ t[i]:
            i += 1
        __ i __ ls_s:
            r_ shift > 0
        __ shift __ 0:
            i += 1
        w.. i < ls_s and s[i] __ t[i + shift]:
            i += 1
        r_ i __ ls_s