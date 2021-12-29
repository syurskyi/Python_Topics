from typing import List

EAST = "E"
WEST = "W"


___ search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    
    running_max = float("-inf")

    __ direction == EAST:
        start =  len(buildings) - 1
        end = -1
        delta = -1
    else:
        start = 0
        end = len(buildings)
        delta = 1
    
    result = []
    for i in range(start,end,delta):
        building_height = buildings[i]
        __ building_height > running_max:
            result.append(i)

        running_max = max(running_max,building_height)
    

    __ direction == EAST:
        result.reverse()

    return result




__ __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]
