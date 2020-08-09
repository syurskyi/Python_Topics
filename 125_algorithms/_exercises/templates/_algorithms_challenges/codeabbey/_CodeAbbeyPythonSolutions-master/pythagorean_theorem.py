______ ma__

amount_values = int(input())
results = []

___ get_triangle_type(side1, side2, side3
    hypotenuse = ma__.sqrt(side1**2 + side2**2)
    __(side3 < hypotenuse
        r_ "A"
    ____(side3 > hypotenuse
        r_ "O"
    ____
        r_ "R"

for i in range(amount_values
    side1, side2, side3 = map(int, input().split())
    results.append(get_triangle_type(side1,side2, side3))

print(*results)