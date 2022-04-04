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
    
    stars =[]
    ___ line __ r..(width + 1
        stars.a..(line * '*')

    count = 0
    ___ line __ stars:
        __ count % 1 __ 0:
            stars.remove(line)
            count += 1

    r.. stars + l..(r..(stars[1:]