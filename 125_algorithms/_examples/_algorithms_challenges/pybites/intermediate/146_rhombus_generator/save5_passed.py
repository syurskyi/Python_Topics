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
    
    stars =[]
    for line in range(width + 1):
        stars.append(line * '*')

    count = 0
    for line in stars:
        if count % 1 == 0:
            stars.remove(line)
            count += 1

    output = [line.center(len(stars[-1]), ' ') for line in stars]

    return output + list(reversed(output))[1:]