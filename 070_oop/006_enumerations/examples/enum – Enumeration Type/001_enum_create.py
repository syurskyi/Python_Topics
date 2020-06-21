# The enum module defines an enumeration type with iteration and comparison capabilities. It can be used to create
# well-defined symbols for values, instead of using literal integers or strings.
# Creating Enumerations
# A new enumeration is defined using the class syntax by subclassing Enum and adding class attributes describing
# the values.

# enum_create.py
import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

# The members of the Enum are converted to instances as the class is parsed. Each instance has a name property
# corresponding to the member name and a value property corresponding to the value assigned to the name
# in the class definition.

# Member name: wont_fix
# Member value: 4
