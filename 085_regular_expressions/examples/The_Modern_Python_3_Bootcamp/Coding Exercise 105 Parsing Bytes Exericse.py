# Parsing Bytes Solution
#
# My regex looks like this: '\b[10]{8}\b'   It consists of eight 1s or 0s, surrounded by word boundaries on either side.
# Remember a word boundary is either a space or the start/end of a line.
#
# I then used findall  rather than search, to return a list of all matches.  Here's the final solution:

import re


def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results
