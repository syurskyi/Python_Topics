class Solution:
    ___ getHint(self, secret, guess
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        __ not secret or not guess or le.(secret) != le.(guess
            r_ ''

        TMPL = '{}A{}B'
        bulls = 0
        cows = 0
        cnts = [0] * 10

        for i in range(le.(secret)):
            s = ord(secret[i]) - ord('0')
            g = ord(guess[i]) - ord('0')

            __ s __ g:
                bulls += 1
                continue

            cnts[s] += 1
            cnts[g] -= 1

            __ cnts[s] <= 0:
                cows += 1
            __ cnts[g] >= 0:
                cows += 1

        r_ TMPL.format(bulls, cows)


class Solution:
    ___ getHint(self, secret, guess
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        __ not secret or not guess or le.(secret) != le.(guess
            r_ ''

        TMPL = '{}A{}B'
        bulls = 0
        cows = 0
        cnt_s = [0] * 10
        cnt_g = [0] * 10

        for i in range(le.(secret)):
            __ secret[i] __ guess[i]:
                bulls += 1
            ____
                cnt_s[int(secret[i])] += 1
                cnt_g[int(guess[i])] += 1

        for i in range(10
            cows += min(cnt_s[i], cnt_g[i])

        r_ TMPL.format(bulls, cows)
