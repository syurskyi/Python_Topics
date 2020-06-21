# Extremes Solution
#
# This solution is pretty straightforward:
#
#     I call min(nums) and max(nums)
#     I wrap the values I get back in a new tuple and return it!


def extremes(nums):
    return (min(nums), max(nums))


