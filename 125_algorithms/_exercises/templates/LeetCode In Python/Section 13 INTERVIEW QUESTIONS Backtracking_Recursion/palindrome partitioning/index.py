c_ Solution:
    ___ isPalin seg
        i _ 0
        j _ le.(seg)-1
        w___(i < j
            __(seg[i] !_ seg[j]
                r_ F..
            i +_ 1
            j -_ 1
        r_ T..

    ___ dfs s: st.
        __(le.(s) __ 0 a.. le.(.temp) > 0
            .res.ap..(.temp[:])
            r_
        n _ le.(s)+1
        ___ i __ ra..(1, n
            seg _ s[0:i]
            __(.isPalin(seg)):
                .temp.ap..(seg)
                .dfs(s[i:])
                .temp.p..

    ___ partition s: st.)  L..[L..[st.]]:
        .res _   # list
        .temp _   # list
        .dfs(s)
        r_ .res
