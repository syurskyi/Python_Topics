# zip(), lists, tuples

# list is a sequence type
# list can hold heterogenous elements
# list is mutable - can expand, shrink, elements can be modified
# list is iterable

# tuple is a sequence type
# tuple can hold heterogeneous data
# tuple is immutable
# tuple is iterable

# Test case 1 - when iterables are of equal length
___ test_case1
    list1 = [ 1, 2, 3]
    list2 = [ 'a', 'b', 'c']
    list3 = [ 'red', 'blue', 'green']

    result = z..(list1, list2, list3)
    print(t..(result))

    ___ e __ result:
        print(e)
        print(t..(e))

# Test case 2 - when iterables are of unequal length
___ test_case2
    list1 = [ 1, 2, 3]
    list2 = [ 'a', 'b', 'c']
    list3 = [ 'red', 'blue']

    result = z..(list1, list2, list3)
    print(t..(result))

    ___ e __ result:
        print(e)
        print(t..(e))



test_case2()

