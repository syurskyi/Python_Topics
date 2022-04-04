____ t___ _______ L..

EAST = "E"
WEST = "W"


___ search_apartment(buildings: L..[i..], direction: s..) __ L..[i..]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    
    running_max = f__("-inf")

    __ direction __ EAST:
        start =  l..(buildings) - 1
        end = -1
        delta = -1
    ____:
        start = 0
        end = l..(buildings)
        delta = 1
    
    result    # list
    ___ i __ r..(start,end,delta
        building_height = buildings[i]
        __ building_height > running_max:
            result.a..(i)

        running_max = m..(running_max,building_height)
    

    __ direction __ EAST:
        result.r..

    r.. result




__ _______ __ _______
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"  # [0, 1, 4]
    print(search_apartment(A, "E"  # [4, 6, 7]
    print(search_apartment(B, "W"  # [0, 5]
    print(search_apartment(B, "E"  # [5]
