___ route_diff(directions
    output    # list
    ___ i __ directions:
        __ i __ "N":
            __ output.c.. "S") > 0:
                output.remove("S")
            ____:
                output.a..(i)
        ____ i __ "E":
            __ output.c.. "W") > 0:
                output.remove("W")
            ____:
                output.a..(i)
        ____ i __ "S":
            __ output.c.. "N") > 0:
                output.remove("N")
            ____:
                output.a..(i)
        ____ i __ "W":
            __ output.c.. "E") > 0:
                output.remove("E")
            ____:
                output.a..(i)

    r.. l..(directions) - l..(output)
