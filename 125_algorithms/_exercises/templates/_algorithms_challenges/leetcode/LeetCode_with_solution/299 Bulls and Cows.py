____ c.. _______ defaultdict

__author__ = 'Daniel'


c_ Solution(o..
    ___ getHint  secret, guess
        """
        Need to revert B

        Example:
        1121
        2323

        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt = defaultdict(i..)
        A = 0
        B = 0
        ___ c __ secret:
            cnt[c] += 1

        ___ i, v __ e..(guess
            __ v __ secret[i]:
                A += 1
                __ cnt[v] > 0:
                    cnt[v] -= 1
                ____:
                    B -= 1

            ____ cnt[v] > 0:
                B += 1
                cnt[v] -= 1

        r.. "%dA%dB" % (A, B)


__ _______ __ _______
    ... Solution().getHint("0", "1") __ "0A0B"
