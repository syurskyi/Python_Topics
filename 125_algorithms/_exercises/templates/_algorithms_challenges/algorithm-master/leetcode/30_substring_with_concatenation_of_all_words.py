c_ Solution:
    ___ findSubstring  s, S
        """
        :type s: str
        :type S: List[str]
        :rtype: List[int]
        """
        ans    # list
        __ n.. s o. n.. S o. l..(s) < l..(S) * l..(S[0]
            r.. ans

        n, m, k l..(s), l..(S), l..(S 0
        F    # dict
        ___ c __ S:
            F[c] F.g.. c, 0) + 1

        ___ start __ r..(k
            _F    # dict
            cnt 0
            left start

            ___ right __ r..(start, n - k + 1, k
                sr s[right:right + k]
                __ sr n.. __ F:
                    _F    # dict
                    cnt 0
                    left right + k
                    _____

                _F[sr] _F.g.. sr, 0) + 1
                __ _F[sr] <_ F[sr]:
                    cnt += 1
                w.... _F[sr] > F[sr]:
                    sl s[left:left + k]
                    __ _F[sl] __ F[sl]:
                        cnt -_ 1
                    _F[sl] -_ 1
                    left += k

                __ cnt __ m:
                    ans.a..(left)
                    sl s[left:left + k]
                    cnt -_ 1
                    _F[sl] -_ 1
                    left += k

        r.. ans
