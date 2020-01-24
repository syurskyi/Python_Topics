# Removing Negatives Solution
#
#     I define remove_negatives, which accepts a list I call nums
#     Then I call filter, passing the nums list and a lambda which returns True if an item is greater or equal to 0.
#     This filters out all the values that are negative
#     However filter doesn't return a list, so I have to cast it into a list and then return it


def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))
