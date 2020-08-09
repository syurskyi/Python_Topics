___ route_diff(directions
    output = []
    for i in directions:
        __ i __ "N":
            __ output.count("S") > 0:
                output.remove("S")
            ____
                output.append(i)
        ____ i __ "E":
            __ output.count("W") > 0:
                output.remove("W")
            ____
                output.append(i)
        ____ i __ "S":
            __ output.count("N") > 0:
                output.remove("N")
            ____
                output.append(i)
        ____ i __ "W":
            __ output.count("E") > 0:
                output.remove("E")
            ____
                output.append(i)

    r_ le.(directions) - le.(output)
