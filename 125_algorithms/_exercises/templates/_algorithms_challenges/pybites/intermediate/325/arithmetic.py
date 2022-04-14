____ t___ _______ G..

VALUES "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


___ calc_sums(values: s.. VALUES) __ G..[s.., N.., N..]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    values_list VALUES.s..("[]").s..(", ")
    ___ i __ r..(1, l..(values_list:
        
        previous, current f__(values_list[i -1]), f__(values_list[i])
        __ previous < 0.1 a.. current < 0.1:
            total previous + current
        ____
            total r..(previous, 2) + r..(current, 2)

        y.. f"The sum of {values_list[i -1]} and {values_list[i]}, rounded to two decimal places, is {total:.2f}."


# if __name__ == "__main__":
#     test = calc_sums()
#     print(next(test))
#     print(next(test))
#     print(next(test))
#     print(next(test))
#     print(next(test))