class Solution:
    # @return a boolean
    ___ isMatch(self, s, p):
        __ n.. p:
            r.. n.. s
        __ n.. s:
            r.. False
        r.. self.is_match_aux(s, p, 0, 0)

    ___ is_match_aux(self, s, p, si, pi):
        __ pi __ l..(p):
            r.. si __ l..(s)
        # Next char is not *
        # pi may be the last char
        __ pi < l..(p) - 1 a.. p[pi + 1] != '*' o. pi __ l..(p) - 1:
            ... p[pi] != '*'
            # si must be in bound
            is_cur_matched = si < l..(s) a.. (p[pi] __ s[si] o. p[pi] __ '.')
            is_next_matched = self.is_match_aux(s, p, si + 1, pi + 1)
            r.. is_cur_matched a.. is_next_matched
        # Next char is *
        w.... si < l..(s) a.. pi < l..(p) a.. (p[pi] __ s[si] o. p[pi] __ '.'):
            __ self.is_match_aux(s, p, si, pi + 2):
                r.. True
            si += 1
        r.. self.is_match_aux(s, p, si, pi + 2)


s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "aa")
print s.isMatch("aaa", "aa")
print s.isMatch("aa", "a*")
print s.isMatch("aa", ".*")
print s.isMatch("ab", ".*")
print s.isMatch("aab", "c*a*b")
