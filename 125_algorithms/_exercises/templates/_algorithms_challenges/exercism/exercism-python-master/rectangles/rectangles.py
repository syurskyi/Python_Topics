from itertools ______ combinations
from re ______ match

___ count(diagram=""
    """count find the number of rectangles in a given diagram"""
    corners = find_char(diagram, '+')
    r_ su.(1 ___ rect in combinations(corners, 4) __ is_rect(rect, diagram))

___ find_char(lines, char
    """find_char returns the location of all the corner characters"""
    r_ [ (row, col)
        ___ row, line in enumerate(lines)
        ___ col, elem in enumerate(line)
        __ elem __ char]

___ is_rect(corners, diagram
    """is_rect determines if a set of corners is a rectangle
    by checking alignment and characters between the corners"""
    (a_r, a_c), (b_r, b_c), (c_r, c_c), (d_r, d_c) = sorted(corners)
    __ not (a_r __ b_r and a_c __ c_c and b_c __ d_c and c_r __ d_r
        r_ False

    horz_regex = '\+[-+]{{{}}}\+'.format( d_c - a_c - 1)
    vert_regex = '\+[|+]{{{}}}\+'.format( d_r - a_r - 1)
    top = ''.join(diagram[a_r][a_c:(d_c+1)])
    bottom = ''.join(diagram[d_r][a_c:(d_c+1)])
    left = ''.join(row[a_c] ___ row in diagram[a_r:(d_r+1)])
    right = ''.join(row[d_c] ___ row in diagram[a_r:(d_r+1)])

    r_ match(horz_regex, top) and match(horz_regex, bottom) and \
        match(vert_regex, right) and match(vert_regex, left)
