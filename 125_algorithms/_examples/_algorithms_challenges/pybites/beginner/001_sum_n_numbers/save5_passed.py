def sum_numbers(numbers=None):
    the_sum = []
    if numbers == None:
        return 5050
    else:
        for n in numbers:
            the_sum.append(n)
        return sum(the_sum)