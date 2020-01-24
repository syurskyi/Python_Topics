# Triple and Filter Solution
#
# For my solution, I chose to use map and filter in combination.


def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x * 3, lst)))
