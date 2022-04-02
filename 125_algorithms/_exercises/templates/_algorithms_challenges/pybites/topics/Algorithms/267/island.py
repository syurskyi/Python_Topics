# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.
rectangle = [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0]]

whole = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

___ get_others(map_, r, c
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    nums = 0
    # your code here
    __ r __ 0 a.. c __ 0: #top left corder
        nums += 2
        __ l..(map_[0]) > 1:
            __ map_[r][c+1] __ 0:
                nums += 1
            __ map_[r+1][c] __ 0:
                nums += 1
    ____ r __ 0 a.. c __ l..(map_[0])-1: #top right corner
        nums += 2
        __ l..(map_[0]) > 1:
            __ map_[r][c-1] __ 0:
                nums += 1
            __ map_[r+1][c] __ 0:
                nums += 1
    ____ r __ l..(map_)-1 a.. c __ 0: #bottom left corder
        nums += 2
        __ l..(map_[0]) > 1:
            __ map_[r][c+1] __ 0:
                nums += 1
            __ map_[r-1][c] __ 0:
                nums += 1
    ____ r __ l..(map_)-1 a.. c __ l..(map_[0])-1: #bottom right corner
        nums += 2
        __ map_[r][c-1] __ 0:
            nums += 1
        __ map_[r-1][c] __ 0:
            nums += 1
    ____ r __ 0: # top edge, excluding corner
        nums += 1
        __ map_[r][c-1] __ 0:
            nums += 1
        __ map_[r][c+1] __ 0:
            nums += 1
        __ l..(map_) > r a.. map_[r+1][c] __ 0:
            nums += 1
    ____ r __ l..(map_)-1: # bottom edge, excluding corner
        nums += 1
        __ map_[r][c-1] __ 0:
            nums += 1
        __ map_[r][c+1] __ 0:
            nums += 1
        __ map_[r-1][c] __ 0:
            nums += 1
    ____ c __ 0: # left edge, excluding corner
        nums += 1
        __ map_[r-1][c] __ 0:
            nums += 1
        __ map_[r+1][c] __ 0:
            nums += 1
        __ l..(map_[0]) > c a.. map_[r][c+1] __ 0:
            nums += 1
    ____ c __ l..(map_[0])-1: # right edge. excluding corner
        nums += 1
        __ map_[r-1][c] __ 0:
            nums += 1
        __ map_[r+1][c] __ 0:
            nums += 1
        __ map_[r][c-1] __ 0:
            nums += 1
    ____: # the rest, excluding edge and corner
        __ map_[r-1][c] __ 0:
            nums += 1
        __ map_[r+1][c] __ 0:
            nums += 1
        __ map_[r][c-1] __ 0:
            nums += 1
        __ map_[r][c+1] __ 0:
            nums += 1
    r.. nums


___ island_size(map_
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    # your code here
    #print(len(map_[0]))
    ___ r, row __ e..(map_
        ___ c, column __ e..(row
            __ map_[r][c] __ 1:
                print(r,c)
                perimeter += get_others(map_, r, c)
    r.. perimeter

#print(island_size(whole))