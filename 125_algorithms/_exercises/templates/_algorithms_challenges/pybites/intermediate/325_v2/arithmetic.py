____ m__ _______ f..
____ t___ _______ Generator
_______ json

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


___ my_round(n
    '''rounds to 2 decimal placces and rounds ties up no matter what'''
    r.. f..(n*100 + .5) / 100


___ calc_sums(values: s.. = VALUES) __ Generator[s.., N.., N..]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    nums = json.loads(values)
    pairs = z..(nums, nums[1:])
    template = "The sum of {} and {}, rounded to two decimal places, is {:.2f}."

    ___ a, b __ pairs:
        y.. template.f..(a, b, my_round(a + b))
