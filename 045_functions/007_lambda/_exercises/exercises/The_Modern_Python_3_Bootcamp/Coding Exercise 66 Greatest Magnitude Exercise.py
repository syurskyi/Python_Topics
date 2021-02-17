# Greatest Magnitude Solution
#
#     To find the greatest magnitude (the greatest distance from 0), I combine max() and abs()
#     I call abs() on each num, and find the maximum resulting value using max()


def max_magnitude(nums):
    return max(abs(num) for num in nums)

