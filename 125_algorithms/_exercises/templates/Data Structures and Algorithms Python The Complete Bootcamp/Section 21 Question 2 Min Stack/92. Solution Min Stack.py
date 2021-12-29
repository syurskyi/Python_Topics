c_ MinStack:

    ___  -
        stack  []
        m..  []

    ___ push  x):
        stack.a..(x)

        __ m..:
            __ x < m..[-1]:
                m...a..(x)
        ____
            m...a..(x)

    ___ pop
        __ stack[-1] __ m..[-1]:
            m...pop()
        stack.pop()

    ___ top
        r_ stack[-1]

    ___ getMin
        r_ m..[-1]


## Example Execution ##
obj  MinStack()
obj.push(10)
obj.push(5)
obj.push(15)
obj.pop()
obj.push(20)

result_top  obj.top()
print("Top Value:", result_top)

result_min  obj.getMin()
print("Minimum Value in Stack:", result_min)