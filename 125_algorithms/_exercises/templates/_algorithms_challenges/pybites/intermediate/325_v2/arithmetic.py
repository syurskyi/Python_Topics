from math import floor
from typing import Generator
import json

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


___ my_round(n):
    '''rounds to 2 decimal placces and rounds ties up no matter what'''
    return floor(n*100 + .5) / 100


___ calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    nums = json.loads(values)
    pairs = zip(nums, nums[1:])
    template = "The sum of {} and {}, rounded to two decimal places, is {:.2f}."

    for a, b in pairs:
        yield template.format(a, b, my_round(a + b))
