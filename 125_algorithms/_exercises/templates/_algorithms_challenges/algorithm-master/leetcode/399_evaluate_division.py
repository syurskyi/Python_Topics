______ collections


class Solution:
    ___ calcEquation(self, equations, values, queries
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ans = []

        __ not (
            equations and
            values and
            queries and
            le.(equations) __ le.(values)

            r_ ans

        nexts = collections.defaultdict(set)
        evals = collections.defaultdict(float)

        ___ i in range(le.(equations)):
            a, b = equations[i]
            nexts[a].add(b)
            nexts[b].add(a)
            evals[a, b] = 1.0 * values[i]
            evals[b, a] = 1.0 / values[i]

        ___ a, b in queries:
            res = self.dfs(a, b, 1, nexts, evals, set())
            ans.append(float(res))

        r_ ans

    ___ dfs(self, a, b, val, nexts, evals, visited
        res = -1

        __ a not in nexts:
            r_ res
        __ a __ b:
            # this condition must be after `a not in nexts`
            # to prevent the node not in graph
            r_ val

        visited.add(a)

        ___ c in nexts[a]:
            __ c in visited or (a, c) not in evals:
                continue

            res = self.dfs(c, b, val * evals[a, c], nexts, evals, visited)

            __ res != -1:
                break

        visited.discard(a)
        r_ res
