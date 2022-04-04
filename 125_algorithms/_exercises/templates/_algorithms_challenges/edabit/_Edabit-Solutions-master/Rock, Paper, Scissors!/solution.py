___ calculate_score(games
    abigail  0
    ben  0
    index  0
    w.... index < l..(games
        __ games[index][0] __ "R" a.. games[index][1] __ "S":
            abigail + 1

        ____ games[index][0] __ "P" a.. games[index][1] __ "R":
            abigail + 1
        ____ games[index][0] __ "S" a.. games[index][1] __ "P":
            abigail + 1

        ____ games[index][0] __ "S" a.. games[index][1] __ "R":
            ben += 1
        ____ games[index][0] __ "R" a.. games[index][1] __ "P":
            ben += 1
        ____ games[index][0] __ "P" a.. games[index][1] __ "S":
            ben += 1
        index += 1

    __ abigail > ben:
        r.. "Abigail"
    ____ abigail __ ben:
        r.. "Tie"
    ____
         r.. "Benson"
