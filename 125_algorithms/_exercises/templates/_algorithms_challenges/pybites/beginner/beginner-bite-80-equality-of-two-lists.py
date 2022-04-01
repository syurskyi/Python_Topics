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

____ enum _______ Enum

c_ Equality(Enum):
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
    __ list1 __ list2: r.. Equality.SAME_REFERENCE
    ____ list1 __ list2: r.. Equality.SAME_ORDERED
    ____ l..(list1) __ l..(list2) a.. n.. s..(list1).difference(list2): r.. Equality.SAME_UNORDERED
    ____ l..(s..(list1).symmetric_difference(list2)) __ 0: r.. Equality.SAME_UNORDERED_DEDUPED
    ____:
        r.. Equality.NO_EQUALITY

___ check_equality_solution2(list1, list2):

    __ list1 __ list2:
        r.. Equality.SAME_REFERENCE

    __ list1 __ list2:
        r.. Equality.SAME_ORDERED

    __ s..(list1) __ s..(list2):
        r.. Equality.SAME_UNORDERED

    __ s..(list1) __ s..(list2):
        r.. Equality.SAME_UNORDERED_DEDUPED

    r.. Equality.NO_EQUALITY

l = ['1']
a = [1, 2, 2, 3, 4]
b = a |  + [1, 3, 4, 4]
print(check_equality(l,l))
print(check_equality(['1', '2', '3'], ['1', '2', '3']))
print(check_equality(['1', '3', '2'], ['1', '2', '3']))
print(check_equality(['1'], ['1', '2']))
print(check_equality(a,b))



