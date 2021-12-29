___ route_diff(directions):
    output = []
    for i in directions:
        __ i == "N":
            __ output.count("S") > 0:
                output.remove("S")
            else:
                output.append(i)
        elif i == "E":
            __ output.count("W") > 0:
                output.remove("W")
            else:
                output.append(i)
        elif i == "S":
            __ output.count("N") > 0:
                output.remove("N")
            else:
                output.append(i)
        elif i == "W":
            __ output.count("E") > 0:
                output.remove("E")
            else:
                output.append(i)

    return len(directions) - len(output)
