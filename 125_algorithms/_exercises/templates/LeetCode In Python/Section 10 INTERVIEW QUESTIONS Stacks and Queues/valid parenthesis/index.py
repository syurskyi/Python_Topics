class Solution:
    ___ isEqual(self, c1, c2) -> bool:
        __(c1 __ '(' and c2 __ ')'
            r_ True
        __(c1 __ '[' and c2 __ ']'
            r_ True
        __(c1 __ '{' and c2 __ '}'
            r_ True
        r_ False

    ___ isValid(self, s: str) -> bool:
        st = []
        for character in s:
            __(le.(st) != 0
                li = st[-1]
                __(self.isEqual(li, character)):
                    st.pop()
                    continue
            st.append(characrer)
        r_ le.(st) __ 0
