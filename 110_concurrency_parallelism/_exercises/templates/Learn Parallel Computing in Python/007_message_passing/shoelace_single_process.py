______ __
______ t___
# (45,11),(41,15),(36,20)

PTS_REGEX = "\((\d*),(\d*)\)"


___ find_area(points_str):
    points = []
    area = 0.0
    ___ xy __ __.f..(PTS_REGEX, points_str):
        points.a..((i..(xy.g..(1)), i..(xy.g..(2))))

    ___ i __ r...(l..(points)):
        a, b = points[i], points[(i + 1) % l..(points)]
        area += a[0] * b[1] - a[1] * b[0]
    area = abs(area) / 2.0
    # print(area)


f = o..("polygons.txt", "r")
lines = f.r.. .s...
start = t___.t___()
___ line __ lines:
    find_area(line)
end = t___.t___()
print("Time taken", end - start)
