amount_values = int(input())
results = []

___ get_area(x1, y1, x2, y2, x3, y3
    r_ (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2


___ i in range(amount_values
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    area_of_triangle = get_area(x1,y1,x2,y2,x3,y3)

    __(area_of_triangle < 0
        area_of_triangle *= -1
    results.append(area_of_triangle)

print(*results)

