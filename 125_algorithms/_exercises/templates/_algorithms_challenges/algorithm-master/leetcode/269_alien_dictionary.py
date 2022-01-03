c_ Solution:
    ___ alienOrder(self, words):
        """
        :type words: list[str]
        :rtype: str
        """
        __ n.. words:
            r.. ''

        ans    # list
        gotcha = set()
        max_size = max(l..(word) ___ word __ words)

        ___ j __ r..(max_size):
            ___ word __ words:
                __ j >= l..(word):
                    continue

                __ word[j] __ gotcha:
                    continue

                ans.a..(word[j])
                gotcha.add(word[j])

        r.. ''.j..(ans)


c_ Solution:
    """
    REF: https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs/2
    """
    ___ alienOrder(self, words):
        __ n.. words:
            r.. ''

        ans    # list
        edges    # dict
        indeg    # dict

        ___ w __ words:
            ___ c __ w:
                indeg[c] = 0

        ___ i __ r..(l..(words) - 1):
            cur = words[i]
            nxt = words[i + 1]
            ___ j __ r..(m..(l..(cur), l..(nxt))):
                __ cur[j] __ nxt[j]:
                    continue
                __ cur[j] n.. __ edges:
                    edges[cur[j]] = set()
                __ nxt[j] n.. __ edges[cur[j]]:
                    edges[cur[j]].add(nxt[j])
                    indeg[nxt[j]] = indeg.get(nxt[j], 0) + 1
                break

        queue = [c ___ c, deg __ indeg.i.. __ deg __ 0]
        ___ c __ queue:
            ans.a..(c)
            __ c n.. __ edges:
                continue
            ___ _c __ edges[c]:
                indeg[_c] -= 1
                __ indeg[_c] __ 0:
                    queue.a..(_c)

        r.. ''.j..(ans) __ l..(ans) __ l..(indeg) ____ ''
