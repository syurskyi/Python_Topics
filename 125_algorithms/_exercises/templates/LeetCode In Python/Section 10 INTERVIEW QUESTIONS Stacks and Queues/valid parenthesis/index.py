c_ Solution:
    ___ isEqual(, c1, c2) -> bool:
        __(c1 __ '(' and c2 __ ')'
            r_ True
        __(c1 __ '[' and c2 __ ']'
            r_ True
        __(c1 __ '{' and c2 __ '}'
            r_ True
        r_ False

    ___ isValid(, s: str) -> bool:
        st _ []
        ___ character __ s:
            __(le.(st) !_ 0
                li _ st[-1]
                __(.isEqual(li, character)):
                    st.pop()
                    continue
            st.append(characrer)
        r_ le.(st) __ 0
