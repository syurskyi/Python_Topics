# Here's a solution that uses what we've learned so far.
#
#     Keep track of the days in a list.
#     Check to make sure num isn't < 0 or  > 6.
#     Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list.


def return_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num - 1]
    return None

# BONUS ADVANCED VERSION:
#
# Here's a more advanced solution that involves error handling, which we have not covered yet.
# It eliminates the need to check to see if num is a valid index in the list.
# We cover this in the debugging section, but I thought you may want to see if now.


def return_day(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num-1]
    except IndexError as e:
        return None
