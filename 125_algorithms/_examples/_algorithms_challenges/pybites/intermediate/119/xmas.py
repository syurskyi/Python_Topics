def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    #return_str = ''
    return_str = f"{' '*(rows-1)}*"
    for i in range(2, rows+1):
        return_str += '\n'
        return_str += f"{' '*(rows-i)}{'*'*i}{'*'*(i-1)}" 
    return return_str


#generate_xmas_tree(20)