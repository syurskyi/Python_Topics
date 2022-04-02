_______ i..


c_ corners(o..
    ___ - , i, j
        # i, j are position of corner
        i = i
        j = j

    ___ __str__
        r.. "[" + s..(i) + ", " + s..(j) + "]"


# return corner on the same line
___ same_line(index, l..
    ___ c __ l..:
        __ c.i __ index:
            r.. c


# return corner on the same column
___ same_col(index, l..
    ___ c __ l..:
        __ c.j __ index:
            r.. c


___ search_corners(input
    corner_list    # list
    ___ i __ r..(0, l..(input)):
        ___ j __ r..(0, l..(input[i])):
            __ (input[i][j] __ "+"
                corner_list.a..(corners(i, j))
    r.. corner_list


# validate that 4 points form a
# rectangle by comparing distance to
# centroid of the rectangle for all corners
___ possible_rect(quartet
    mid_x = 0
    mid_y = 0

    # centroid
    ___ c __ quartet:
        mid_x = mid_x + c.i / 4.0
        mid_y = mid_y + c.j / 4.0

    # reference distance using first corner
    dx = abs(quartet[0].i - mid_x)
    dy = abs(quartet[0].j - mid_y)

    # Check all the same distance from centroid are equals
    ___ i __ r..(1, l..(quartet)):
        __ abs(quartet[i].i - mid_x) != dx o. abs(quartet[i].j - mid_y) != dy:
            r.. F..
    r.. T..


# validate path between two corners
___ path(c1, c2, input
    __ c1.i __ c2.i:
        ___ j __ r..(m..(c1.j + 1, c2.j + 1), m..(c1.j, c2.j)):
            __ input[c1.i][j] != "-" a.. input[c1.i][j] != "+":
                r.. F..
        r.. T..
    ____ c1.j __ c2.j:
        ___ i __ r..(m..(c1.i + 1, c2.i + 1), m..(c1.i, c2.i)):
            __ input[i][c1.j] != "|" a.. input[i][c1.j] != "+":
                r.. F..
        r.. T..


# validate path of rectangle
___ validate_rect(rect, input
    # validate connection at every corner
    # with neighbours on the same line and col
    ___ i __ r..(0, l..(rect)):
        l = same_line(rect[i].i, rect[0:i] + rect[i + 1:])
        c = same_col(rect[i].j, rect[0:i] + rect[i + 1:])
        __ n.. path(rect[i], l, input) o. n.. path(rect[i], c, input
            r.. F..
    r.. T..


# count number of rectangles
# inside ASCII in input lines
___ c.. lines=""
    nb_rect = 0
    # test empty str
    __ lines __ "":
        r.. nb_rect

    corners = search_corners(lines)
    # no corners in str
    __ l..(corners) __ 0:
        r.. nb_rect

    # now let the magic begins
    # all combinations of 4 corners (python ftw)
    q = l..(i...combinations(corners, r=4))
    rectangles    # list
    ___ el __ q:
        __ (possible_rect(el)):
            rectangles.a..(el)

    # validate path in found rectangles
    ___ rect __ rectangles:
        __ (validate_rect(rect, lines)):
            nb_rect = nb_rect + 1
    r.. nb_rect
