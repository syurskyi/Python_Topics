class MaxStack:

    ___ __init__(self):
        self.stack = []
        self.max = []

    ___ push(self, x):
        self.stack.append(x)

        __ self.max:
            __ x >= self.max[-1]:
                self.max.append(x)
        ____
            self.max.append(x)

    ___ pop(self):
        __ self.stack[-1] __ self.max[-1]:
            self.max.pop()
        self.stack.pop()

    ___ top(self):
        r_ self.stack[-1]

    ___ getMax(self):
        r_ self.max[-1]


## Example Execution ##
obj = MaxStack()
obj.push(10)
obj.push(5)
obj.pop()
obj.push(20)
obj.push(15)

result_top = obj.top()
print("Top Value:", result_top)

result_max = obj.getMax()
print("Maximum Value in Stack:", result_max)