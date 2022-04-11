c_ Solution:
    ___ getHint  secret, guess
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        __ n.. secret o. n.. guess o. l..(secret) != l..(guess
            r.. ''

        TMPL '{}A{}B'
        bulls 0
        cows 0
        cnts [0] * 10

        ___ i __ r..(l..(secret:
            s o..(secret[i]) - o..('0')
            g o..(guess[i]) - o..('0')

            __ s __ g:
                bulls += 1
                _____

            cnts[s] += 1
            cnts[g] -_ 1

            __ cnts[s] <_ 0:
                cows += 1
            __ cnts[g] >_ 0:
                cows += 1

        r.. TMPL.f..(bulls, cows)


c_ Solution:
    ___ getHint  secret, guess
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        __ n.. secret o. n.. guess o. l..(secret) != l..(guess
            r.. ''

        TMPL '{}A{}B'
        bulls 0
        cows 0
        cnt_s [0] * 10
        cnt_g [0] * 10

        ___ i __ r..(l..(secret:
            __ secret[i] __ guess[i]:
                bulls += 1
            ____
                cnt_s[i..(secret[i])] += 1
                cnt_g[i..(guess[i])] += 1

        ___ i __ r..(10
            cows += m..(cnt_s[i], cnt_g[i])

        r.. TMPL.f..(bulls, cows)
