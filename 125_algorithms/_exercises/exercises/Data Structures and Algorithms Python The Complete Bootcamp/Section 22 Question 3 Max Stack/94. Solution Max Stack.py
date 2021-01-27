class MaxStack:

    ___  -
        stack = []
        max = []

    ___ push  x):
        stack.append(x)

        __ max:
            __ x >= max[-1]:
                max.append(x)
        ____
            max.append(x)

    ___ pop
        __ stack[-1] __ max[-1]:
            max.pop()
        stack.pop()

    ___ top
        r_ stack[-1]

    ___ getMax
        r_ max[-1]


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