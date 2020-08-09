c_ MinStack:
    ___ __init__(
        .st _ []

    ___ push(, x: int) -> None:
        curMin _ .getMin()
        __ curMin __ None o.. curMin > x:
            curMin _ x
        .st.append((x, curMin))

    ___ pop() -> None:
        .st.pop()

    ___ top() -> int:
        r_ .st[-1][0] __ .st else None

    ___ getMin() -> int:
        r_ .st[-1][1] __ .st else None
