STAR = '*'

___ gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    stars = [(line * 2 - 1) * '*' ___ line __ r..(width - 1)]
    stacked = [line.center(l..(stars[-1]), ' ') ___ line __ stars[1:]]
    stacked_rev = [item ___ item __ reversed(stacked)]
    y.. stacked + stacked_rev[1:]