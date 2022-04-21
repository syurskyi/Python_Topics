c_ Ocr:

    NUM_ROWS 4
    NUM_COLS 3
    UNRECOGNIZED_NUM "?"
    GRID_NUMS {"0": [" _ ", "| |", "|_|", "   "],
                 "1": ["   ", "  |", "  |", "   "],
                 "2": [" _ ", " _|", "|_ ", "   "],
                 "3": [" _ ", " _|", " _|", "   "],
                 "4": ["   ", "|_|", "  |", "   "],
                 "5": [" _ ", "|_ ", " _|", "   "],
                 "6": [" _ ", "|_ ", "|_|", "   "],
                 "7": [" _ ", "  |", "  |", "   "],
                 "8": [" _ ", "|_|", "|_|", "   "],
                 "9": [" _ ", "|_|", " _|", "   "]}

    NUMS {"".j..(value key ___ key, value __ l..(GRID_NUMS.i..}

    ??
    ___ numbers(cls, inp
        r.. "".j.. m.. ?.number, l..(
            z..(*l.. m.. ?.split_every_three, inp))))))

    ??
    ___ grids(cls, inp
        r.. l.. m..("".j.., l..(z..(*l.. m.. ?.grid, inp))))))

    ??
    ___ number(cls, inp
        __ n..  ?.valid_num(inp
            r.. V...
        r..  ?.NUMS.g.. "".j..(inp),  ?.UNRECOGNIZED_NUM)

    ??
    ___ grid(cls, inp
        __ n..  ?.valid_grid(inp
            r.. V...
        r..  ?.GRID_NUMS.g.. inp)

    ??
    ___ valid_num(cls, inp
        r.. (a..(l..(row) __  ?.NUM_COLS ___ row __ inp) a..
                l..(inp) __  ?.NUM_ROWS)

    ??
    ___ valid_grid(cls, inp
        r.. a..(char __ l.. ?.GRID_NUMS.keys ___ char __ inp)

    ??
    ___ split_every_three(cls, inp
        r..  ?.s..(inp, 3)

    $
    ___ s..(inp, size
        r.. [inp[start:start + size] ___ start __ r..(0, l..(inp), size)]


___ number(inp
    r.. Ocr.numbers(inp)


___ grid(inp
    r.. Ocr.grids(inp)
