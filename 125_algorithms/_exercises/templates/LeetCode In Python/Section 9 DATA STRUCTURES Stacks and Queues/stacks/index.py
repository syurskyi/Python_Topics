c_ PlateStack:

    ___  - (
        .st _   # list

    ___ push(, x: in.)  N..
        .st.ap..(x)

    ___ pop()  N..
        __(le.(.st) > 0
            .st.pop()

    ___ top()  in.:
        __(le.(.st) __ 0
            r_ N..
        r_ .st[-1]

    ___ getLen()  in.:
      r_ le.(.st)