"""
Main Concept:

in product case, needs to remove product in last recursion, and adds the product in current.
"""


c_ Solution:
    ___ addOperators  s, target
        """
        :type s: str
        :type target: int
        :rtype: List[str]
        """
        ans    # list

        __ n.. s:
            r.. ans

        dfs(s, 0, target, 0, 0, ans, [])
        r.. ans

    ___ dfs  s, start, target, val, multi, ans, p..
        __ start __ l..(s) a.. target __ val:
            ans.a..(''.j..(p..))
            r..
        __ start > l..(s
            r..

        ___ i __ r..(start, l..(s)):
            __ i > start a.. s[start] __ '0':
                # only allow i == start and its `0`
                _____

            sa  s[start:i + 1]
            a  i..(sa)

            __ start __ 0:
                dfs(s, i + 1, target, a, a, ans, [sa])
                _____

            dfs(s, i + 1, target, val + a, a, ans, p.. +  '+', sa])
            dfs(s, i + 1, target, val - a, -a, ans, p.. +  '-', sa])
            dfs(s, i + 1, target, val - multi + multi * a, multi * a, ans, p.. +  '*', sa])
