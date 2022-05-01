c_ Solution:
    ___ alienOrder  words
        """
        :type words: list[str]
        :rtype: str
        """
        __ n.. words:
            r.. ''

        ans    # list
        gotcha s..()
        max_size m..(l.. ? ___ word __ words)

        ___ j __ r..(max_size
            ___ word __ words:
                __ j >_ l..(word
                    _____

                __ word[j] __ gotcha:
                    _____

                ans.a..(word[j])
                gotcha.add(word[j])

        r.. ''.j..(ans)


c_ Solution:
    """
    REF: https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs/2
    """
    ___ alienOrder  words
        __ n.. words:
            r.. ''

        ans    # list
        edges    # dict
        indeg    # dict

        ___ w __ words:
            ___ c __ w:
                indeg[c] 0

        ___ i __ r..(l..(words) - 1
            cur words[i]
            nxt words[i + 1]
            ___ j __ r..(m..(l..(cur), l..(nxt))):
                __ cur[j] __ nxt[j]:
                    _____
                __ cur[j] n.. __ edges:
                    edges[cur[j]] s..()
                __ nxt[j] n.. __ edges[cur[j]]:
                    edges[cur[j]].add(nxt[j])
                    indeg[nxt[j]] indeg.g.. nxt[j], 0) + 1
                _____

        queue [c ___ c, deg __ indeg.i.. __ deg __ 0]
        ___ c __ queue:
            ans.a..(c)
            __ c n.. __ edges:
                _____
            ___ _c __ edges[c]:
                indeg[_c] -_ 1
                __ indeg[_c] __ 0:
                    queue.a..(_c)

        r.. ''.j..(ans) __ l..(ans) __ l..(indeg) ____ ''
