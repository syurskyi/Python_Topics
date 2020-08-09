______ itertools


class corners(object
    ___ __init__(self, i, j
        # i, j are position of corner
        self.i = i
        self.j = j

    ___ __str__(self
        r_ "[" + str(self.i) + ", " + str(self.j) + "]"


# return corner on the same line
___ same_line(index, list
    for c in list:
        __ c.i __ index:
            r_ c


# return corner on the same column
___ same_col(index, list
    for c in list:
        __ c.j __ index:
            r_ c


___ search_corners(input
    corner_list = []
    for i in range(0, le.(input)):
        for j in range(0, le.(input[i])):
            __ (input[i][j] __ "+"
                corner_list.append(corners(i, j))
    r_ corner_list


# validate that 4 points form a
# rectangle by comparing distance to
# centroid of the rectangle for all corners
___ possible_rect(quartet
    mid_x = 0
    mid_y = 0

    # centroid
    for c in quartet:
        mid_x = mid_x + c.i / 4.0
        mid_y = mid_y + c.j / 4.0

    # reference distance using first corner
    dx = abs(quartet[0].i - mid_x)
    dy = abs(quartet[0].j - mid_y)

    # Check all the same distance from centroid are equals
    for i in range(1, le.(quartet)):
        __ abs(quartet[i].i - mid_x) != dx or abs(quartet[i].j - mid_y) != dy:
            r_ False
    r_ True


# validate path between two corners
___ path(c1, c2, input
    __ c1.i __ c2.i:
        for j in range(min(c1.j + 1, c2.j + 1), max(c1.j, c2.j)):
            __ input[c1.i][j] != "-" and input[c1.i][j] != "+":
                r_ False
        r_ True
    ____ c1.j __ c2.j:
        for i in range(min(c1.i + 1, c2.i + 1), max(c1.i, c2.i)):
            __ input[i][c1.j] != "|" and input[i][c1.j] != "+":
                r_ False
        r_ True


# validate path of rectangle
___ validate_rect(rect, input
    # validate connection at every corner
    # with neighbours on the same line and col
    for i in range(0, le.(rect)):
        l = same_line(rect[i].i, rect[0:i] + rect[i + 1:])
        c = same_col(rect[i].j, rect[0:i] + rect[i + 1:])
        __ not path(rect[i], l, input) or not path(rect[i], c, input
            r_ False
    r_ True


# count number of rectangles
# inside ASCII in input lines
___ count(lines=""
    nb_rect = 0
    # test empty str
    __ lines __ "":
        r_ nb_rect

    corners = search_corners(lines)
    # no corners in str
    __ le.(corners) __ 0:
        r_ nb_rect

    # now let the magic begins
    # all combinations of 4 corners (python ftw)
    q = list(itertools.combinations(corners, r=4))
    rectangles = []
    for el in q:
        __ (possible_rect(el)):
            rectangles.append(el)

    # validate path in found rectangles
    for rect in rectangles:
        __ (validate_rect(rect, lines)):
            nb_rect = nb_rect + 1
    r_ nb_rect
