c_ MinStack
    ___  -
        .st _   # list

    ___ push x: in.)  N..
        curMin _ .getMin()
        __ curMin __ N.. o.. curMin > x:
            curMin _ x
        .st.ap..((x, curMin))

    ___ p..  N..
        .st.p..

    ___ top()  in.:
        r_ .st[-1][0] __ .st ____  N..

    ___ getMin()  in.:
        r_ .st[-1][1] __ .st ____  N..
