IMPOSSIBLE = 'Mission impossible. No one can contribute.'

poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
extreme = [-1, -2, -3, -4, -5, -1, -2, -3]
some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
community = [3, 2, 6,  4, 7,  5, -8, -9, 3,  8,  4, -12, 3, -10, -15,
             2, 6, -10, 6, 3, -1,  5, -5, -8, 11, 7, -9, -5,  -6, -2,
             7, 8, 11, 8,  6, -1, -6,  9, 8, 6, -3, 4,  -8, 3, -4, 1,
             2, 8, -2, 9, -3, 8, -10,  -8,  5,  -4, -6,  5, -1, 4, 2,
             2, 7,  3, -2, 5, 1, 4, -7, 5, 8, 4, 2, 10, -24, -10, -9,
             -2, 1, 6, 1,  3, -44, 3, 6, -1, 9, -6, 5, 4, 3, 6, -1,
             0, 11, 4, 8, 16, -33, 8, -2, 4, 5, 3, 2, -8, -7, -5,
             0, 2, 5, -2, 4, 1, 2, 4, 2, -5, 7, 4, 5, -2, 7, 5, -8]


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    best_sum, total, starting, ending = 0, 0, 0, 0
    for index in range(len(village)):
        total = 0
        for i in range(len(village[index:])):
            total += village[index+i]
            if total >= best_sum:
                best_sum = total
                starting = index
                ending = index+i
    if best_sum == 0:
        return (best_sum, starting, ending)
    else:
        return (best_sum, starting+1, ending+1)

print(max_fund(community))
print(max_fund(poverty))
print(max_fund(some))
print(max_fund(extreme))