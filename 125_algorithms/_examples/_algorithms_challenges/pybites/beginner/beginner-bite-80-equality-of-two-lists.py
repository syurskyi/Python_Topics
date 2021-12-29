'''
Bite 80. Check equality of two lists
In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

Complete the check_equality function returning the various Enum values (representing equality scores) according to the type of equality of the lists:

return SAME_REFERENCE if both lists reference the same object,
return SAME_ORDERED if they have the same content and order,
return SAME_UNORDERED if they have the same content unordered,
return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,
and finally return NO_EQUALITY if none of the previous cases match.
'''

from enum import Enum

class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0



def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if list1 is list2: return Equality.SAME_REFERENCE
    elif list1 == list2: return Equality.SAME_ORDERED
    elif len(list1) == len(list2) and not set(list1).difference(list2): return Equality.SAME_UNORDERED
    elif len(set(list1).symmetric_difference(list2)) == 0: return Equality.SAME_UNORDERED_DEDUPED
    else:
        return Equality.NO_EQUALITY

def check_equality_solution2(list1, list2):

    if list1 is list2:
        return Equality.SAME_REFERENCE

    if list1 == list2:
        return Equality.SAME_ORDERED

    if sorted(list1) == sorted(list2):
        return Equality.SAME_UNORDERED

    if set(list1) == set(list2):
        return Equality.SAME_UNORDERED_DEDUPED

    return Equality.NO_EQUALITY

l = ['1']
a = [1, 2, 2, 3, 4]
b = a[:] + [1, 3, 4, 4]
print(check_equality(l,l))
print(check_equality(['1', '2', '3'], ['1', '2', '3']))
print(check_equality(['1', '3', '2'], ['1', '2', '3']))
print(check_equality(['1'], ['1', '2']))
print(check_equality(a,b))



