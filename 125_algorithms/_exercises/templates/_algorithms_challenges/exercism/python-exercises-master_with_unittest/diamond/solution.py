___ make_diamond(letter):
    rows = o..(letter) - 64
    cols = rows * 2 - 1
    half = make_half(rows, cols)
    r.. ''.j..(half + half[-2::-1])


___ make_half(rows, cols):
    diamond_half    # list
    ___ x __ r..(rows):
        row = [' '] * cols
        row[rows - 1 - x] = chr(x + 65)
        row[rows - 1 + x] = chr(x + 65)
        diamond_half.a..(''.j..(row) + '\n')
    r.. diamond_half
