IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    

    best_sum = current_sum =  0

    best_start = best_end = current_start= current_end = -1

    for i,value in enumerate(village):
        value = village[i]
        if value >= current_sum + value:
            current_start= current_end = i
            current_sum = value
        else:
            current_sum += value
            current_end += 1


        if current_sum > best_sum:
            best_sum = current_sum
            best_start,best_end = current_start,current_end


    if best_sum == 0:
        print(IMPOSSIBLE)


    return (best_sum,best_start + 1,best_end + 1)




        






