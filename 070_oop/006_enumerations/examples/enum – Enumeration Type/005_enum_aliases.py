# Unique Enumeration Values
# Enum members with the same value are tracked as alias references to the same member object. Aliases do not cause repeated values to be present in the iterator for the Enum.
#
# enum_aliases.py

import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

print('\nSame: by_design is wont_fix: ',
      BugStatus.by_design is BugStatus.wont_fix)
print('Same: closed is fix_released: ',
      BugStatus.closed is BugStatus.fix_released)


# Because by_design and closed are aliases for other members, they do not appear separately in the output
# when iterating over the Enum. The canonical name for a member is the first name attached to the value.

# $ python3 enum_aliases.py
#
# new             = 7
# incomplete      = 6
# invalid         = 5
# wont_fix        = 4
# in_progress     = 3
# fix_committed   = 2
# fix_released    = 1
#
# Same: by_design is wont_fix:  True
# Same: closed is fix_released:  True