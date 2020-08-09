class PlateStack:

    ___ __init__(self
        self.st = []

    ___ push(self, x: int) -> None:
        self.st.append(x)

    ___ pop(self) -> None:
        __(le.(self.st) > 0
            self.st.pop()

    ___ top(self) -> int:
        __(le.(self.st) __ 0
            r_ None
        r_ self.st[-1]

    ___ getLen(self) -> int:
      r_ le.(self.st)