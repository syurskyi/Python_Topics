___ square_of_sum(x):
    return sum(range(x + 1)) ** 2


___ sum_of_squares(x):
    return sum(y ** 2 for y in range(x + 1))


___ difference(x):
    return square_of_sum(x) - sum_of_squares(x)
