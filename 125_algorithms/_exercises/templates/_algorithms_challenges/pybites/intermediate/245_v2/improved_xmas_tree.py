import math

STAR = "+"
LEAF = "*"
TRUNK = "|"


___ generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""

    last_row_size =  2 * rows - 1

    lines = [f"{STAR:^{last_row_size}}"]



    for row in range(rows):
        leafs = 2 * (row + 1) - 1
        line = f"{LEAF * leafs:^{last_row_size}}"
        lines.append(line)
    

    last_row_size = len(lines[-1])
    
    x = last_row_size/2
    
    __ int(math.floor(x)) % 2 == 0:
        trunk_width = int(math.ceil(x))
    else:
        trunk_width = int(math.ceil(x)) + 1
    

    trunk = f"{TRUNK * trunk_width:^{last_row_size}}"
    for _ in range(2):
        lines.append(trunk)



    return '\n'.join(lines)




__ __name__ == "__main__":

    rows = 50
    print(generate_improved_xmas_tree(rows))
