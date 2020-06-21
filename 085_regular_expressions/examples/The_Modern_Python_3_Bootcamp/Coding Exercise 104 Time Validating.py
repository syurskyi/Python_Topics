# Time Validating Solution
#
# The regular expression I used is:
#
#     ^\d\d?:\d\d$
#
# The time must start with a digit, and there can be a second optional digit before the colon.
# Then there's the colon and two mandatory digits.
# I used ^ and $ to make sure the time was the only thing in the input string.
#
# Here's the full solution:

import re


def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False
