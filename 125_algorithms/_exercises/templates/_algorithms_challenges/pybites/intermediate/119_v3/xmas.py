___ generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    
    result = []
    stars = 1

    final_row_stars =  2 * rows - 1

    left_gap = final_row_stars//2


    for row in range(1,rows + 1): 
        
        stars = 2 * row - 1
        left_gap += 1
        line = f"{'*'*stars:>{left_gap}}\n"
        __ row == rows:
            line = line.rstrip()
        result.append(line)


    return ''.join(result)


__ __name__ == "__main__":

    print(generate_xmas_tree())
