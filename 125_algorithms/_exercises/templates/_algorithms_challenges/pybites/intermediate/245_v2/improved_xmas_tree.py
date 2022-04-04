_______ m__

STAR = "+"
LEAF = "*"
TRUNK = "|"


___ generate_improved_xmas_tree(rows=10
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""

    last_row_size =  2 * rows - 1

    lines = [f"{STAR:^{last_row_size}}"]



    ___ row __ r..(rows
        leafs = 2 * (row + 1) - 1
        line = f"{LEAF * leafs:^{last_row_size}}"
        lines.a..(line)
    

    last_row_size = l..(lines[-1])
    
    x = last_row_size/2
    
    __ i..(m__.f..(x % 2 __ 0:
        trunk_width = i..(m__.ceil(x
    ____:
        trunk_width = i..(m__.ceil(x + 1
    

    trunk = f"{TRUNK * trunk_width:^{last_row_size}}"
    ___ _ __ r..(2
        lines.a..(trunk)



    r.. '\n'.j..(lines)




__ _______ __ _______

    rows = 50
    print(generate_improved_xmas_tree(rows
