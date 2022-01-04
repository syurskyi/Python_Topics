____ typing _______ List

EAST = "E"
WEST = "W"


___ search_apartment(buildings: List[i..], direction: s..) __ List[i..]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    highest = 0
    building_list    # list
    __ direction __ "E":
        buildings.reverse()
    ___ index, building __ e..(buildings):
        __ building > highest:
            highest = building
            building_list.a..(index)
    __ direction __ "E":
        ___ index, building __ e..(building_list):
            building_list[index] = l..(buildings)-building-1
        building_list.reverse()
    r.. building_list



__ _______ __ _______
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]