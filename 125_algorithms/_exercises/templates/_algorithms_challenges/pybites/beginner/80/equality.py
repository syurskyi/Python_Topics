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
    __ list1 __ list2:
        r.. Equality.SAME_REFERENCE
    ____ list1 __ list2:
        r.. Equality.SAME_ORDERED
    ____ s..(list1) __ s..(list2):
        r.. Equality.SAME_UNORDERED
    ____ l..(d...f..(list1)) __ l..(d...f..(list2)):
        r.. Equality.SAME_UNORDERED_DEDUPED
    ____ list1 != list2:
        r.. Equality.NO_EQUALITY

