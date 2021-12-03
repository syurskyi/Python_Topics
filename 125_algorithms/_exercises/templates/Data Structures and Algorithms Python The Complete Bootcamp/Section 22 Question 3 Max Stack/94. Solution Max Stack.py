c_ MaxStack:

    ___  -
        stack = []
        ma_ = []

    ___ push  x):
        stack.append(x)

        __ ma_:
            __ x >= ma_[-1]:
                ma_.append(x)
        ____
            ma_.append(x)

    ___ pop
        __ stack[-1] __ ma_[-1]:
            ma_.pop()
        stack.pop()

    ___ top
        r_ stack[-1]

    ___ getMax
        r_ ma_[-1]


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