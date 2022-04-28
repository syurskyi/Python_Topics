c_ Solution o..
    ___ numIslands2  m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # quick union find with weights
        ans = []
        islands = Union()
        ___ p __ map(tuple, positions):
            islands.add(p)
            ___ dp __ (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                __ q __ islands.id:
                    islands.unite(p, q)
            ans += [islands.count]
        r_ ans

c_ Union o..
    """
    quick union find with weights
    """
    ___ -(self):
        # use dic to reduce index operations
        id  # dict
        sz  # dict
        count = 0

    ___ add  p):
        id[p] = p
        sz[p] = 1
        count += 1

    ___ root  i):
        w.. i != id[i]:
            id[i] = id[id[i]]
            i = id[i]
        r_ i

    ___ unite  p, q):
        i, j = root(p), root(q)
        __ i __ j:
            r_
        __ sz[i] > sz[j]:
            i, j = j, i
        id[i] = j
        sz[j] += sz[i]
        count -= 1