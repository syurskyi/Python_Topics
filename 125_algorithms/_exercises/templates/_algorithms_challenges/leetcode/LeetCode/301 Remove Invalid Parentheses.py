"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""
__author__ = 'Daniel'


class Solution(object
    ___ removeInvalidParentheses(self, s
        """
        Brute force: BFS and then validate

        Algorithm focuses on left parentheses
        Backtracking/DFS with prune & jump

        :type s: str
        :rtype: List[str]
        """
        rmcnt = self.minrm(s)
        ret = []
        self.dfs(s, "", 0, None, 0, rmcnt, ret)
        r_ ret

    ___ minrm(self, s
        """
        Find the minimal removal count to limit the search depth
        returns minimal number of removals
        """
        rmcnt = 0
        left = 0
        for c in s:
            __ c __ "(":
                left += 1
            ____ c __ ")":
                __ left > 0:
                    left -= 1
                ____
                    rmcnt += 1

        rmcnt += left
        r_ rmcnt

    ___ dfs(self, s, cur, left, pi, i, rmcnt, ret
        """
        Remove parenthesis
        backtracking, post-check
        :param s: original string
        :param cur: current string builder
        :param left: number of remaining left parentheses in s[0..i] not consumed by ")"
        :param pi: last removed char
        :param i: current index
        :param rmcnt: number of remaining removals needed
        :param ret: results
        """
        __ left < 0 or rmcnt < 0 or i > le.(s
            r_
        __ i __ le.(s
            __ rmcnt __ 0 and left __ 0:
                ret.append(cur)
            r_

        __ s[i] not in ("(", ")"  # skip non-parenthesis
            self.dfs(s, cur+s[i], left, None, i+1, rmcnt, ret)
        ____
            __ pi __ s[i]:  # jump, if rm, rm them all to avoid duplication
                w___ i < le.(s) and pi and pi __ s[i]: i, rmcnt = i+1, rmcnt-1
                self.dfs(s, cur, left, pi, i, rmcnt, ret)
            ____
                self.dfs(s, cur, left, s[i], i+1, rmcnt-1, ret)
                L = left+1 __ s[i] __ "(" else left-1  # consume "("
                self.dfs(s, cur+s[i], L, None, i+1, rmcnt, ret)  # put


__ __name__ __ "__main__":
    assert Solution().removeInvalidParentheses("(a)())()") __ ['(a())()', '(a)()()']
