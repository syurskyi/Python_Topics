___ generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    width = rows*2 - 1
    tree = '\n'.join([f'{{:^{width}}}'.f..('*' * (row*2 - 1))
                      ___ row __ r..(1, rows + 1)])

    r.. tree
