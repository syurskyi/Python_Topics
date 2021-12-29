class Solution:
    ___ getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        __ not secret or not guess or len(secret) != len(guess):
            return ''

        TMPL = '{}A{}B'
        bulls = 0
        cows = 0
        cnts = [0] * 10

        for i in range(len(secret)):
            s = ord(secret[i]) - ord('0')
            g = ord(guess[i]) - ord('0')

            __ s == g:
                bulls += 1
                continue

            cnts[s] += 1
            cnts[g] -= 1

            __ cnts[s] <= 0:
                cows += 1
            __ cnts[g] >= 0:
                cows += 1

        return TMPL.format(bulls, cows)


class Solution:
    ___ getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        __ not secret or not guess or len(secret) != len(guess):
            return ''

        TMPL = '{}A{}B'
        bulls = 0
        cows = 0
        cnt_s = [0] * 10
        cnt_g = [0] * 10

        for i in range(len(secret)):
            __ secret[i] == guess[i]:
                bulls += 1
            else:
                cnt_s[int(secret[i])] += 1
                cnt_g[int(guess[i])] += 1

        for i in range(10):
            cows += min(cnt_s[i], cnt_g[i])

        return TMPL.format(bulls, cows)
