_______ c..


c_ Solution:
    ___ calcEquation  equations, values, queries
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ans    # list

        __ n.. (
            equations a..
            values a..
            queries a..
            l..(equations) __ l..(values)

            r.. ans

        nexts = c...d..(s..)
        evals = c...d..(f__)

        ___ i __ r..(l..(equations)):
            a, b = equations[i]
            nexts[a].add(b)
            nexts[b].add(a)
            evals[a, b] = 1.0 * values[i]
            evals[b, a] = 1.0 / values[i]

        ___ a, b __ queries:
            res = dfs(a, b, 1, nexts, evals, s..
            ans.a..(f__(res))

        r.. ans

    ___ dfs  a, b, val, nexts, evals, visited
        res = -1

        __ a n.. __ nexts:
            r.. res
        __ a __ b:
            # this condition must be after `a not in nexts`
            # to prevent the node not in graph
            r.. val

        visited.add(a)

        ___ c __ nexts[a]:
            __ c __ visited o. (a, c) n.. __ evals:
                _____

            res = dfs(c, b, val * evals[a, c], nexts, evals, visited)

            __ res != -1:
                _____

        visited.discard(a)
        r.. res
