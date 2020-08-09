class Solution:
    # @return a boolean
    ___ isMatch(self, s, p
        __ not p:
            r_ not s
        __ not s:
            r_ False
        r_ self.is_match_aux(s, p, 0, 0)

    ___ is_match_aux(self, s, p, si, pi
        __ pi __ le.(p
            r_ si __ le.(s)
        # Next char is not *
        # pi may be the last char
        __ pi < le.(p) - 1 and p[pi + 1] != '*' or pi __ le.(p) - 1:
            assert p[pi] != '*'
            # si must be in bound
            is_cur_matched = si < le.(s) and (p[pi] __ s[si] or p[pi] __ '.')
            is_next_matched = self.is_match_aux(s, p, si + 1, pi + 1)
            r_ is_cur_matched and is_next_matched
        # Next char is *
        w___ si < le.(s) and pi < le.(p) and (p[pi] __ s[si] or p[pi] __ '.'
            __ self.is_match_aux(s, p, si, pi + 2
                r_ True
            si += 1
        r_ self.is_match_aux(s, p, si, pi + 2)


s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "aa")
print s.isMatch("aaa", "aa")
print s.isMatch("aa", "a*")
print s.isMatch("aa", ".*")
print s.isMatch("ab", ".*")
print s.isMatch("aab", "c*a*b")
