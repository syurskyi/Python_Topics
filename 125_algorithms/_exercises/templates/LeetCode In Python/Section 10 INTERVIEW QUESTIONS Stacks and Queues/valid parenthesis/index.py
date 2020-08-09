c_ Solution:
    ___ isEqual(, c1, c2) -> bool:
        __(c1 __ '(' a.. c2 __ ')'
            r_ T..
        __(c1 __ '[' a.. c2 __ ']'
            r_ T..
        __(c1 __ '{' a.. c2 __ '}'
            r_ T..
        r_ F..

    ___ isValid(, s: st.) -> bool:
        st _ []
        ___ character __ s:
            __(le.(st) !_ 0
                li _ st[-1]
                __(.isEqual(li, character)):
                    st.pop()
                    continue
            st.ap..(characrer)
        r_ le.(st) __ 0
