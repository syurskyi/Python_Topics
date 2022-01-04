_______ __

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1
STOP = ' '

___ _seek_next(grid: l.., position: tuple):
    row, col = position
    next_val = grid[row][col] + 1
    __ row < l..(grid)-1 a.. grid[row + 1][col] __ next_val:
        r.. (row + 1, col), DOWN
    __ row > 0 a.. grid[row - 1][col] __ next_val:
        r.. (row - 1, col), UP
    __ col < l..(grid[row])-1 a.. grid[row][col + 1] __ next_val:
        r.. (row, col + 1), RIGHT
    __ col > 0 a.. grid[row][col - 1] __ next_val:
        r.. (row, col - 1), LEFT
    r.. (row, col), STOP


___ print_sequence_route(grid: s.., start_coordinates_ N..
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    grid_array = [[i..(v) ___ v __ __.f..(r'(\d+)', line)]
                  ___ line __ grid.splitlines(keepends=F..)
                  __ l..(line.r..('|', '').strip()) > 0]

    start_coordinates = [(row, col)
                         ___ row __ r..(l..(grid_array))
                         ___ col __ r..(l..(grid_array[row]))
                         __ grid_array[row][col] __ START_VALUE][0]

    current_direction = RIGHT
    current_vals = [s..(START_VALUE)]

    this_val = START_VALUE + 1
    next_coordinates = start_coordinates
    w.... current_direction != STOP:
        next_coordinates, next_direction = _seek_next(grid_array, next_coordinates)
        __ current_direction __ next_direction:
            current_vals.a..(s..(this_val))
        ____:
            print(f'{" ".j..(current_vals)} {next_direction}')
            current_vals = [s..(this_val)]
            current_direction = next_direction
        this_val += 1

    print('done')
