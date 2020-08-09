c_ PlateStack:

    ___ __init__(
        .st _ []

    ___ push(, x: int) -> None:
        .st.append(x)

    ___ pop() -> None:
        __(le.(.st) > 0
            .st.pop()

    ___ top() -> int:
        __(le.(.st) __ 0
            r_ None
        r_ .st[-1]

    ___ getLen() -> int:
      r_ le.(.st)