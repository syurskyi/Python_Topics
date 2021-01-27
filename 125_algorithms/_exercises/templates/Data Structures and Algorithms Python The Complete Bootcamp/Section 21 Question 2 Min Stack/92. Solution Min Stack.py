class MinStack:

    ___ __init__(self):
        self.stack = []
        self.min = []

    ___ push(self, x):
        self.stack.append(x)

        __ self.min:
            __ x <= self.min[-1]:
                self.min.append(x)
        ____
            self.min.append(x)

    ___ pop(self):
        __ self.stack[-1] __ self.min[-1]:
            self.min.pop()
        self.stack.pop()

    ___ top(self):
        r_ self.stack[-1]

    ___ getMin(self):
        r_ self.min[-1]


## Example Execution ##
obj = MinStack()
obj.push(10)
obj.push(5)
obj.push(15)
obj.pop()
obj.push(20)

result_top = obj.top()
print("Top Value:", result_top)

result_min = obj.getMin()
print("Minimum Value in Stack:", result_min)