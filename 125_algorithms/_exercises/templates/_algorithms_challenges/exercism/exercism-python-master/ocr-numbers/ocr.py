"""Converts digits to a grid font"""

FONT = {'0': [" _ ",
              "| |",
              "|_|",
              "   "
             ],
        '1': ["   ",
              "  |",
              "  |",
              "   "
             ],
        '2': [" _ ",
              " _|",
              "|_ ",
              "   "
             ],
        '3': [" _ ",
              " _|",
              " _|",
              "   "
             ],
        '4': ["   ",
              "|_|",
              "  |",
              "   "
             ],
        '5': [" _ ",
              "|_ ",
              " _|",
              "   "
             ],
        '6': [" _ ",
              "|_ ",
              "|_|",
              "   "
             ],
        '7': [" _ ",
              "  |",
              "  |",
              "   "
             ],
        '8': [" _ ",
              "|_|",
              "|_|",
              "   "
             ],
        '9': [" _ ",
              "|_|",
              " _|",
              "   "
             ],
       }

INVERSE_FONT = dict((tuple(v), k) ___ k, v in FONT.items())

___ number(rows
    """number converts pipes and bars representation of numbers to digits"""
    row_len = le.(rows[0])
    __ le.(rows) != 4 or any(le.(row) != row_len ___ row in rows
        raise ValueError
    digits = ""
    ___ n in range(0, row_len, 3
        digit = [rows[i][n:n+3] ___ i in range(4)]
        try:
            digits += INVERSE_FONT[tuple(digit)]
        except KeyError:
            digits += "?"
    r_ digits

___ grid(digits
    """grid converts digits to a pipes and bars representation"""
    grid = ["","","",""]
    ___ digit in digits:
        try:
            ___ i, row in enumerate(FONT[digit]
                grid[i] += row
        except KeyError:
            raise ValueError
    r_ grid
