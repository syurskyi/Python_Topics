# Comparing Enums
# Because enumeration members are not ordered, they support only comparison by identity and equality.
# enum_comparison.py

import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print('Identity:',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Ordered by value:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Cannot sort: {}'.format(err))

# The greater-than and less-than comparison operators raise TypeError exceptions.

# $ python3 enum_comparison.py
#
# Equality: False True
# Identity: False True
# Ordered by value:
#   Cannot sort: '<' not supported between instances of 'BugStatus
# ' and 'BugStatus'