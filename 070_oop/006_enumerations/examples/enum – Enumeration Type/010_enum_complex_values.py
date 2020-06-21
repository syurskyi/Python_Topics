# For more complex cases, tuples might become unwieldy. Since member values can be any type of object, dictionaries
# can be used for cases where there are a lot of separate attributes to track for each enum value.
# Complex values are passed directly to __init__() as the only argument other than self.

# enum_complex_values.py

import enum

class BugStatus(enum.Enum):

    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }
    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }
    invalid = {
        'num': 5,
        'transitions': ['new'],
    }
    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }
    in_progress = {
        'num': 3,
        'transitions': ['new', 'fix_committed'],
    }
    fix_committed = {
        'num': 2,
        'transitions': ['in_progress', 'fix_released'],
    }
    fix_released = {
        'num': 1,
        'transitions': ['new'],
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print('Name:', BugStatus.in_progress)
print('Value:', BugStatus.in_progress.value)
print('Custom attribute:', BugStatus.in_progress.transitions)
print('Using attribute:', BugStatus.in_progress.can_transition(BugStatus.new))


# This example expresses the same data as the previous example, using dictionaries rather than tuples.
#
# $ python3 enum_complex_values.py
#
# Name: BugStatus.in_progress
# Value: {'num': 3, 'transitions': ['new', 'fix_committed']}
# Custom attribute: ['new', 'fix_committed']
# Using attribute: True