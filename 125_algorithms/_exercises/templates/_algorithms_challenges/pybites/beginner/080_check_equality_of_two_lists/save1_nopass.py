from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


___ check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    equality_number = 0
    # SAME_REFERENCE
    __ list1 == list2:
        equality_number += 1
    # SAME_ORDERED
    __ sorted(list1) == sorted(list2):
        equality_number += 1
    # SAME_UNORDERED
    __ set(list1) == set(list2):
        equality_number += 1
    # SAME_UNORDERED_DEDUPED
    __ set(sorted(list1)) == set(sorted(list2)):
        equality_number += 1
    return Equality(equality_number)