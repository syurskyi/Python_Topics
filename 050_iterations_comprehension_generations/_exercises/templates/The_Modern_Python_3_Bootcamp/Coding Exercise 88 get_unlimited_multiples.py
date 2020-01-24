# Get Unlimited Multiples Solution
#
# This is similar to previous exercise, except it's simpler! We just loop forever (while True)
# instead of checking to see how many times we've looped.


def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num