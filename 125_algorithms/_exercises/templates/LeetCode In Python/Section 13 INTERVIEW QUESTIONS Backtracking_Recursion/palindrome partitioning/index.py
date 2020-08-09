c_ Solution:
    ___ isPalin(, seg
        i _ 0
        j _ le.(seg)-1
        w___(i < j
            __(seg[i] !_ seg[j]
                r_ False
            i +_ 1
            j -_ 1
        r_ True

    ___ dfs(, s: str
        __(le.(s) __ 0 and le.(.temp) > 0
            .res.append(.temp[:])
            r_
        n _ le.(s)+1
        ___ i __ ra..(1, n
            seg _ s[0:i]
            __(.isPalin(seg)):
                .temp.append(seg)
                .dfs(s[i:])
                .temp.pop()

    ___ partition(, s: str) -> L..[L..[str]]:
        .res _ []
        .temp _ []
        .dfs(s)
        r_ .res
