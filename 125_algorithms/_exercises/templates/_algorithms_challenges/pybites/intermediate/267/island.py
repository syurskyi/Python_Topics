# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


___ get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    
    map_[r][c] = '#'
    nums = 0

    ___ n_row,n_col __ ((r +1,c),(r -1,c),(r,c +1),(r,c-1)):
        in_bounds = 0 <= n_row < l..(map_) a.. 0 <= n_col < l..(map_[0])
        __ in_bounds a.. map_[n_row][n_col] __ 1:
            nums += get_others(map_,n_row,n_col)
        ____ (in_bounds a.. map_[n_row][n_col] __ 0) o. (n.. in_bounds):
            nums += 1









    r.. nums


___ island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0


    # your code here
    ___ row __ r..(l..(map_)):
        ___ col __ r..(l..(map_[0])):
            __ map_[row][col] __ 1:
                perimeter += get_others(map_,row,col)


    r.. perimeter
