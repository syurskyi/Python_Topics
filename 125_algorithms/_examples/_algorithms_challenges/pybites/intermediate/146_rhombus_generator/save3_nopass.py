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
    stars = [(line * 2 - 1) * '*' for line in range(width - 1)]
    stacked = [line.center(len(stars[-1]), ' ') for line in stars[1:]]
    stacked_rev = [item for item in reversed(stacked)]
    return stacked + stacked_rev[1:]