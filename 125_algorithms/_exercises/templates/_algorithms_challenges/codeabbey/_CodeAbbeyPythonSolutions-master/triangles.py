amount_values = i..(input())
results    # list

___ is_triangle(sides
    __(sides[0] + sides[1] < sides[2]
        r.. 0
    ____(sides[1] + sides[2] < sides[0]
        r.. 0
    ____(sides[0] + sides[2] < sides[1]
        r.. 0
    ____:
        r.. 1

___ i __ r..(amount_values
    sides = l.. m..(i.., input().s..()))
    results.a..(is_triangle(sides))

print(*results)

