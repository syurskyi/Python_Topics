
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

    
    left_padding = width//2 + 1
    i = 1
    
    diff = 2
    j = 1
    lines = []
    while i > 0:
        space_before = (width - i)//2
        spaces = ' ' * space_before
        line = f"{spaces}{STAR * i}{spaces}"
        yield line
        #line = f"{STAR * i:>{left_padding}}"
        #yield line
        left_padding += (diff - j)
        i += diff

        if i == width:
            diff = -2
            j = -1


if __name__ == "__main__":

    import argparse


    ap = argparse.ArgumentParser("rhombus generator")

    ap.add_argument("-w","--width",type=int,required=True,help="width of rhombus")

    args = vars(ap.parse_args())
    width = args["width"]
    gen_rhombus(width)





