___ generate_xmas_tree(rows=10
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree_stars = [(line * 2 - 1) * '*'
                  ___ line __ r..(rows + 1)]

    tree = [line.center(l..(tree_stars[-1]), ' ')
            ___ line __ tree_stars[1:]]

    r.. '\n'.j..(tree)
