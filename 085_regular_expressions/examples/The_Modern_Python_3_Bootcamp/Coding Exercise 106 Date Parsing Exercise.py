# Date Parsing Solution
#
# My regex for dates looks like this:
#
# ^(\d\d)[,/.](\d\d)[,/.](\d{4})$
#
# Two digits followed by either a comma, slash, or period.  Then two more digits followed by either a comma, slash,
# or period.  And then 4 more digits.  I used parens to form capture groups for the 3 sections.
#
# Then, I simply referenced those capture groups using match.group(1) or match.group(2), etc.

import re


def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None
