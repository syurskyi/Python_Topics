_____ math


c_ Point:

    ___  -   x, y
        x  x
        y  y


# Euclidean distance - we can omit the square-root function
___ distance(p, q
    r_ math.sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y))


# it has quadratic running time so we want to do better
___ brute_force(sub_array
    # initialize the min_distance to INF
    min_distance  fl__('inf')

    # we have to calculate the distance between every single point
    # we make sure that do not consider the same points multiple times
    # d(a,b) = d(b,a)
    ___ i __ ra__(le_(sub_array) - 1
        ___ j __ ra__(i + 1, le_(sub_array)):
            actual_distance  distance(sub_array[i], sub_array[j])
            __ actual_distance < min_distance:
                min_distance  actual_distance

    r_ min_distance


___ get_strip_delta(strip_points, delta
    min_distance  delta
    n  le_(strip_points)

    # in worst case len(strip_point) = N
    ___ i __ ra__(n
        j  i + 1
        # a geometric packing argument shows that this loop iterates at most 7 times
        # THIS IS WHY WE HAVE SORTED THE POINTS BASED ON Y COORDINATE
        w__ j < n a__ (strip_points[j].y - strip_points[i].y) < min_distance:
            min_distance  distance(strip_points[j], strip_points[i])
            j  j + 1

    r_ min_distance


___ closest_pairs_algorithm(list_sorted_x, list_sorted_y, num_of_items
    # when the number of items smaller than 3 then we use brute-force
    # base case
    __ num_of_items < 5:
        r_ brute_force(list_sorted_x)

    middle_index  num_of_items // 2
    middle_item  list_sorted_x[middle_index]

    # DIVIDE PHASE
    delta_left  closest_pairs_algorithm(list_sorted_x[:middle_index], list_sorted_y, middle_index)
    delta_right  closest_pairs_algorithm(list_sorted_x[middle_index:], list_sorted_y, num_of_items - middle_index)

    delta  min(delta_left, delta_right)

    # CONQUER PHASE - usually this is where the magic happens
    strip_points  []

    ___ i __ ra__(num_of_items
        __ abs(list_sorted_y[i].x - middle_item.x) < delta:
            strip_points.ap..(list_sorted_y[i])

    strip_delta  get_strip_delta(strip_points, delta)

    r_ min(strip_delta, delta)


___ run(list1, list2
    list1.sort(keylambda point: point.x)
    list2.sort(keylambda point: point.y)
    r_ closest_pairs_algorithm(list1, list2, le_(list1))


__ ___ __ '__main__':
    points  [Point(1, 1), Point(4, 2), Point(10, 10), Point(1, 2), Point(5, 3)]

    l1  li__(points)
    l2  li__(points)

    print(run(l1, l2))
