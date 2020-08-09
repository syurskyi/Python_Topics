c_ PlateStack:

    ___ __init__(
        .st _ []

    ___ push(, x: in.) -> None:
        .st.ap..(x)

    ___ pop() -> None:
        __(le.(.st) > 0
            .st.pop()

    ___ top() -> in.:
        __(le.(.st) __ 0
            r_ None
        r_ .st[-1]

    ___ getLen() -> in.:
      r_ le.(.st)