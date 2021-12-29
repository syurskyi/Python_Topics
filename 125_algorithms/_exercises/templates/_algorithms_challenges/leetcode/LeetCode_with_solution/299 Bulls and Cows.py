from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    ___ getHint(self, secret, guess):
        """
        Need to revert B

        Example:
        1121
        2323

        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt = defaultdict(int)
        A = 0
        B = 0
        for c in secret:
            cnt[c] += 1

        for i, v in enumerate(guess):
            __ v == secret[i]:
                A += 1
                __ cnt[v] > 0:
                    cnt[v] -= 1
                else:
                    B -= 1

            elif cnt[v] > 0:
                B += 1
                cnt[v] -= 1

        return "%dA%dB" % (A, B)


__ __name__ == "__main__":
    assert Solution().getHint("0", "1") == "0A0B"
