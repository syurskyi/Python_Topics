STAR = "+"
LEAF = "*"
TRUNK = "|"


___ generate_improved_xmas_tree(rows=10
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    width = rows * 2 - 1
    out = [f'{STAR:^{width}}'
    ___ n __ r..(rows
        out.a.. _*{LEAF * (n * 2 + 1^{width}}')
    trunk = TRUNK * (rows + (1 __ rows % 2 __ 0 ____ 0))
    out.a.. _*{trunk:^{width}}')
    out.a.. _*{trunk:^{width}}')
    r.. '\n'.j..(out)
