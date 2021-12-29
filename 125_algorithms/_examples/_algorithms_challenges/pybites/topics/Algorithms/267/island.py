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

def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    nums = 0
    # your code here
    if r == 0 and c == 0: #top left corder
        nums += 2
        if len(map_[0]) > 1:
            if map_[r][c+1] == 0:
                nums += 1
            if map_[r+1][c] == 0:
                nums += 1
    elif r == 0 and c == len(map_[0])-1: #top right corner
        nums += 2
        if len(map_[0]) > 1:
            if map_[r][c-1] == 0:
                nums += 1
            if map_[r+1][c] == 0:
                nums += 1
    elif r == len(map_)-1 and c == 0: #bottom left corder
        nums += 2
        if len(map_[0]) > 1:
            if map_[r][c+1] == 0:
                nums += 1
            if map_[r-1][c] == 0:
                nums += 1
    elif r == len(map_)-1 and c == len(map_[0])-1: #bottom right corner
        nums += 2
        if map_[r][c-1] == 0:
            nums += 1
        if map_[r-1][c] == 0:
            nums += 1
    elif r == 0: # top edge, excluding corner
        nums += 1
        if map_[r][c-1] == 0:
            nums += 1
        if map_[r][c+1] == 0:
            nums += 1
        if len(map_) > r and map_[r+1][c] == 0:
            nums += 1
    elif r == len(map_)-1: # bottom edge, excluding corner
        nums += 1
        if map_[r][c-1] == 0:
            nums += 1
        if map_[r][c+1] == 0:
            nums += 1
        if map_[r-1][c] == 0:
            nums += 1
    elif c == 0: # left edge, excluding corner
        nums += 1
        if map_[r-1][c] == 0:
            nums += 1
        if map_[r+1][c] == 0:
            nums += 1
        if len(map_[0]) > c and map_[r][c+1] == 0:
            nums += 1
    elif c == len(map_[0])-1: # right edge. excluding corner
        nums += 1
        if map_[r-1][c] == 0:
            nums += 1
        if map_[r+1][c] == 0:
            nums += 1
        if map_[r][c-1] == 0:
            nums += 1
    else: # the rest, excluding edge and corner
        if map_[r-1][c] == 0:
            nums += 1
        if map_[r+1][c] == 0:
            nums += 1
        if map_[r][c-1] == 0:
            nums += 1
        if map_[r][c+1] == 0:
            nums += 1
    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    # your code here
    #print(len(map_[0]))
    for r, row in enumerate(map_):
        for c, column in enumerate(row):
            if map_[r][c] == 1:
                print(r,c)
                perimeter += get_others(map_, r, c)
    return perimeter

#print(island_size(whole))