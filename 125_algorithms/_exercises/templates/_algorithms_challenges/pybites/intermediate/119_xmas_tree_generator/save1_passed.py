___ generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree_stars = [(line * 2 - 1) * '*'
                  for line in range(rows + 1)]

    tree = [line.center(len(tree_stars[-1]), ' ')
            for line in tree_stars[1:]]

    return '\n'.join(tree)
