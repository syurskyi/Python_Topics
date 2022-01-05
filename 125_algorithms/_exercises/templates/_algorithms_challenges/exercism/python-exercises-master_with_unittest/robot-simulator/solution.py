NORTH, EAST, SOUTH, WEST = r..(4)


c_ Compass(o..):
    compass = [NORTH, EAST, SOUTH, WEST]

    ___ - , bearing=NORTH):
        bearing = bearing

    ___ left
        bearing = compass[bearing - 1]

    ___ right
        bearing = compass[(bearing + 1) % 4]


c_ Robot(o..):
    ___ - , bearing=NORTH, x=0, y=0):
        compass = Compass(bearing)
        x = x
        y = y

    ___ advance
        __ bearing __ NORTH:
            y += 1
        ____ bearing __ SOUTH:
            y -= 1
        ____ bearing __ EAST:
            x += 1
        ____ bearing __ WEST:
            x -= 1

    ___ turn_left
        compass.left()

    ___ turn_right
        compass.right()

    ___ simulate  commands):
        instructions = {'A': advance,
                        'R': turn_right,
                        'L': turn_left}
        ___ cmd __ commands:
            __ cmd __ instructions:
                instructions[cmd]()

    $
    ___ bearing
        r.. compass.bearing

    $
    ___ coordinates
        r.. (x, y)
