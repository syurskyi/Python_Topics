import collections


class Solution:
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    ___ isCyclicGraph(self, start, end):
        __ not start or not end or len(start) != len(end):
            return False

        n = len(start)
        nxt = collections.defaultdict(set)
        visited = set()
        rec_stack = set()

        for i in range(n):
            nxt[start[i]].add(end[i])

        for i in range(n):
            __ start[i] in visited:
                continue
            __ self.dfs(start[i], nxt, visited, rec_stack):
                return True

        return False

    ___ dfs(self, u, nxt, visited, rec_stack):
        __ u not in nxt:
            return False

        visited.add(u)
        rec_stack.add(u)

        for v in nxt[u]:
            __ v in rec_stack:
                return True

            __ v not in visited and self.dfs(v, nxt, visited, rec_stack):
                return True

        rec_stack.discard(u)
        return False
