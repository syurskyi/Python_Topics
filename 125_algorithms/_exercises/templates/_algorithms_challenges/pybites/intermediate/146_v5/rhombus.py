STAR = '*'


___ gen_rhombus(width
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
    half = width // 2
    ___ n __ r..(width
        __ n < half:
            y.. (STAR * (2 * n + 1.center(width, ' ')
        ____
            y.. (STAR * (2 * (width - n) - 1.center(width, ' ')
