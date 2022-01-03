_______ collections


c_ Solution:
    ___ calcEquation(self, equations, values, queries):
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
        ):
            r.. ans

        nexts = collections.defaultdict(set)
        evals = collections.defaultdict(float)

        ___ i __ r..(l..(equations)):
            a, b = equations[i]
            nexts[a].add(b)
            nexts[b].add(a)
            evals[a, b] = 1.0 * values[i]
            evals[b, a] = 1.0 / values[i]

        ___ a, b __ queries:
            res = dfs(a, b, 1, nexts, evals, set())
            ans.a..(float(res))

        r.. ans

    ___ dfs(self, a, b, val, nexts, evals, visited):
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
                continue

            res = dfs(c, b, val * evals[a, c], nexts, evals, visited)

            __ res != -1:
                break

        visited.discard(a)
        r.. res
