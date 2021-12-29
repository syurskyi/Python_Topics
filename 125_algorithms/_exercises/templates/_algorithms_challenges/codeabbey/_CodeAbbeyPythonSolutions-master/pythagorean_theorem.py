_______ math

amount_values = int(input())
results    # list

___ get_triangle_type(side1, side2, side3):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    __(side3 < hypotenuse):
        r.. "A"
    ____(side3 > hypotenuse):
        r.. "O"
    ____:
        r.. "R"

___ i __ r..(amount_values):
    side1, side2, side3 = map(int, input().split())
    results.a..(get_triangle_type(side1,side2, side3))

print(*results)