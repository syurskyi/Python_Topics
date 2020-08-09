class MinStack:
    ___ __init__(self
        self.st = []

    ___ push(self, x: int) -> None:
        curMin = self.getMin()
        __ curMin __ None or curMin > x:
            curMin = x
        self.st.append((x, curMin))

    ___ pop(self) -> None:
        self.st.pop()

    ___ top(self) -> int:
        r_ self.st[-1][0] __ self.st else None

    ___ getMin(self) -> int:
        r_ self.st[-1][1] __ self.st else None
