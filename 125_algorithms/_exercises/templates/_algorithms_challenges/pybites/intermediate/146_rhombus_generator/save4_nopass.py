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
    
    stars =[]
    for line in range(width + 1):
        stars.append(line * '*')

    count = 0
    for line in stars:
        __ count % 1 == 0:
            stars.remove(line)
            count += 1

    return stars + list(reversed(stars))[1:]