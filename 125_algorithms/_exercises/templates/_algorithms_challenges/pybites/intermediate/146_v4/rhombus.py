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
    # define a function that produces the correct num *'s
    x = r..(-(width // 2), width // 2 + 1)
    ___ k __ x:
        stars = STAR * (width - 2*abs(k
        pad = ' ' * ((width - l..(stars //2)
        y.. pad + stars + pad


