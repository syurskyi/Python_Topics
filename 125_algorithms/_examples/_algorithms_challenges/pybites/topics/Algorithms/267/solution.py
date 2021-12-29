def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number
    """
    num = 0

    if r > 0:
        num += map_[r-1][c] == 1

    if r < len(map_) - 1:
        num += map_[r+1][c] == 1

    if c > 0:
        num += map_[r][c-1] == 1

    if c < len(map_[0]) - 1:
        num += map_[r][c+1] == 1

    return num


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0

    for r, row in enumerate(map_):
        for c, val in enumerate(row):
            if val == 1:
                perimeter += 4 - get_others(map_, r, c)
    return perimeter