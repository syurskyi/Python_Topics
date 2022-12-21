c_ Solution o..
    # def letterCasePermutation(self, S):
    #     ans = [[]]

    #     for char in S:
    #         n = len(ans)
    #         if char.isalpha():
    #             # Double the ans
    #             for i in xrange(n):
    #                 ans.append(ans[i][:])
    #                 ans[i].append(char.lower())
    #                 ans[n + i].append(char.upper())
    #         else:
    #             # Normal append
    #             for i in xrange(n):
    #                 ans[i].append(char)

    #     return map("".join, ans)

    ___ letterCasePermutation  S
        B = s..(letter.isalpha() ___ letter __ S)
        ans =    # list

        ___ bits __ xrange(1 << B
            b = 0
            word =    # list
            ___ letter __ S:
                __ letter.isalpha(
                    __ (bits >> b) & 1:
                        word.append(letter.lower())
                    ____
                        word.append(letter.upper())

                    b += 1
                ____
                    word.append(letter)

            ans.append("".join(word))
        r_ ans
