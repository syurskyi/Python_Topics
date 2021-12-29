STAR = '*'

def gen_rhombus(width):
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
    x = range(-(width // 2), width // 2 + 1)
    for k in x:
        stars = STAR * (width - 2*abs(k))
        pad = ' ' * ((width - len(stars)) //2)
        yield pad + stars + pad


