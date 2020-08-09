c_ MinStack:
    ___ __init__(
        .st _ []

    ___ push(, x: in.) -> None:
        curMin _ .getMin()
        __ curMin __ None o.. curMin > x:
            curMin _ x
        .st.ap..((x, curMin))

    ___ pop() -> None:
        .st.pop()

    ___ top() -> in.:
        r_ .st[-1][0] __ .st else None

    ___ getMin() -> in.:
        r_ .st[-1][1] __ .st else None
