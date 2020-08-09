amount_values = int(input())
results = []

___ is_triangle(sides
    __(sides[0] + sides[1] < sides[2]
        r_ 0
    ____(sides[1] + sides[2] < sides[0]
        r_ 0
    ____(sides[0] + sides[2] < sides[1]
        r_ 0
    ____
        r_ 1

___ i in range(amount_values
    sides = list(map(int, input().split()))
    results.append(is_triangle(sides))

print(*results)

