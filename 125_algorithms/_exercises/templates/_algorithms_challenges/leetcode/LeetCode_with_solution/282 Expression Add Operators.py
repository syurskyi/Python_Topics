"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not
unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
__author__ = 'Daniel'


c_ Solution(o..):
    ___ addOperators  num, target):
        """
        Adapted from https://leetcode.com/discuss/58614/java-standard-backtrace-ac-solutoin-short-and-clear

        Algorithm:
        1. DFS
        2. Special handling for multiplication
        3. Detect invalid number with leading 0's
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret    # list
        dfs(num, target, 0, "", 0, 0, ret)
        r.. ret

    ___ dfs  num, target, pos, cur_str, cur_val, mul, ret):
        __ pos >= l..(num):
            __ cur_val __ target:
                ret.a..(cur_str)
        ____:
            ___ i __ x..(pos, l..(num)):
                __ i != pos a.. num[pos] __ "0":
                    _____
                nxt_val = i..(num[pos:i+1])

                __ n.. cur_str:
                    dfs(num, target, i+1, "%d"%nxt_val, nxt_val, nxt_val, ret)
                ____:
                    dfs(num, target, i+1, cur_str+"+%d"%nxt_val, cur_val+nxt_val, nxt_val, ret)
                    dfs(num, target, i+1, cur_str+"-%d"%nxt_val, cur_val-nxt_val, -nxt_val, ret)
                    dfs(num, target, i+1, cur_str+"*%d"%nxt_val, cur_val-mul+mul*nxt_val, mul*nxt_val, ret)


__ _______ __ _______
    ... Solution().addOperators("232", 8) __ ["2+3*2", "2*3+2"]
