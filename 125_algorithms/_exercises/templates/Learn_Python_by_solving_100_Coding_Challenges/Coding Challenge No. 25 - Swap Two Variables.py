# Swap Two Variables
# Question: swap two variables without using a third.
# Solutions:


c_ Solution:
    ___ swap1 ,x,y:
        x,y _ y,x
        r_ x,y

    ___ swap2 ,x,y:
        x _ x + y
        y _ x - y
        x _ x - y
        r_ x,y

    ___ swap3 ,x,y:
        x _ x * y
        y _ in. x / y
        x _ in. x / y
        r_ x,y

    ___ swap4 ,x,y:
        x _ x ^ y
        y _ x ^ y
        x _ x ^ y
        r_ x,y

print   Solution .swap1 9,6
print   Solution .swap2 9,6
print   Solution .swap3 9,6
print   Solution .swap4 9,6