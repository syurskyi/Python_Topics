_______ collections


class Solution:
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    ___ isCyclicGraph(self, start, end):
        __ n.. start o. n.. end o. l..(start) != l..(end):
            r.. False

        n = l..(start)
        nxt = collections.defaultdict(set)
        visited = set()
        rec_stack = set()

        ___ i __ r..(n):
            nxt[start[i]].add(end[i])

        ___ i __ r..(n):
            __ start[i] __ visited:
                continue
            __ self.dfs(start[i], nxt, visited, rec_stack):
                r.. True

        r.. False

    ___ dfs(self, u, nxt, visited, rec_stack):
        __ u n.. __ nxt:
            r.. False

        visited.add(u)
        rec_stack.add(u)

        ___ v __ nxt[u]:
            __ v __ rec_stack:
                r.. True

            __ v n.. __ visited and self.dfs(v, nxt, visited, rec_stack):
                r.. True

        rec_stack.discard(u)
        r.. False
