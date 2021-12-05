______ re
______ t___
____ _ ______ P.., Queue
# (45,11),(41,15),(36,20)

PTS_REGEX = "\((\d*),(\d*)\)"
TOTAL_PROCESSES = 8


___ find_area(points_queue):
    points_str = points_queue.get()
    while points_str is not None:
        points = []
        area = 0.0
        ___ xy __ re.finditer(PTS_REGEX, points_str):
            points.append((int(xy.group(1)), int(xy.group(2))))

        ___ i __ r...(len(points)):
            a, b = points[i], points[(i + 1) % len(points)]
            area += a[0] * b[1] - a[1] * b[0]
        area = abs(area) / 2.0
        # print(area)
        points_str = points_queue.get()


__ _____ __ _____
    queue = Queue(maxsize=1000)
    processes = []
    ___ i __ r...(TOTAL_PROCESSES):
        p = P..(t.._find_area, a.._(queue,))
        processes.append(p)
        p.s..
    f = open("polygons.txt", "r")
    lines = f.read().splitlines()
    start = t___.t___()
    ___ line __ lines:
        queue.put(line)
    ___ _ __ r...(TOTAL_PROCESSES): queue.put(None)
    ___ p __ processes: p.join()
    end = t___.t___()
    print("Time taken", end - start)
