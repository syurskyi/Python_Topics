# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    
    map_[r][c] = '#'
    nums = 0

    for n_row,n_col in ((r +1,c),(r -1,c),(r,c +1),(r,c-1)):
        in_bounds = 0 <= n_row < len(map_) and 0 <= n_col < len(map_[0])
        if in_bounds and map_[n_row][n_col] == 1:
            nums += get_others(map_,n_row,n_col)
        elif (in_bounds and map_[n_row][n_col] == 0) or (not in_bounds):
            nums += 1









    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0


    # your code here
    for row in range(len(map_)):
        for col in range(len(map_[0])):
            if map_[row][col] == 1:
                perimeter += get_others(map_,row,col)


    return perimeter
