___ generate_xmas_tree(rows=10
   """Generate a xmas tree of stars (*) for given rows (default 10).
      Each row has row_number*2-1 stars, simple example: for rows=3 the
      output would be like this (ignore docstring's indentation):
        *
       ***
      *****"""
   star = "*"
   max_length = rows * 2 -1
   levels = [((row * 2 -1) * star).center(max_length) ___ row __ r..(1, rows +1)]
   r.. "\n".j..(levels)


# if __name__ == "__main__":
#    print(generate_xmas_tree())