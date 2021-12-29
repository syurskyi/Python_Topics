___ get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number
    """
    num = 0

    __ r > 0:
        num += map_[r-1][c] __ 1

    __ r < l..(map_) - 1:
        num += map_[r+1][c] __ 1

    __ c > 0:
        num += map_[r][c-1] __ 1

    __ c < l..(map_[0]) - 1:
        num += map_[r][c+1] __ 1

    r.. num


___ island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0

    ___ r, row __ enumerate(map_):
        ___ c, val __ enumerate(row):
            __ val __ 1:
                perimeter += 4 - get_others(map_, r, c)
    r.. perimeter