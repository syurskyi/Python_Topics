# Extract Full Name Solution
#
# I use map and a lambda to create a new list full of formatted strings:


def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
