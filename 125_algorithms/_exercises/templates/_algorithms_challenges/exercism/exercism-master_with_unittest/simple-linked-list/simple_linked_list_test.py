_______ unittest

____ simple_linked_list _______ LinkedList, EmptyListException


# No canonical data available for this exercise

c_ SimpleLinkedListTest(unittest.TestCase
    ___ test_empty_list_has_len_zero
        sut LinkedList()
        assertEqual(l..(sut), 0)

    ___ test_singleton_list_has_len_one
        sut LinkedList([1])
        assertEqual(l..(sut), 1)

    ___ test_non_empty_list_has_correct_len
        sut LinkedList([1, 2, 3])
        assertEqual(l..(sut), 3)

    ___ test_error_on_empty_list_head
        sut LinkedList()
        w__ assertRaisesWithMessage(EmptyListException
            sut.head()

    ___ test_singleton_list_has_head
        sut LinkedList([1])
        assertEqual(sut.head().value(), 1)

    ___ test_non_empty_list_has_correct_head
        sut LinkedList([1, 2])
        assertEqual(sut.head().value(), 2)

    ___ test_can_push_to_non_empty_list
        sut LinkedList([1, 2, 3])
        sut.push(4)
        assertEqual(l..(sut), 4)

    ___ test_pushing_to_empty_list_changes_head
        sut LinkedList()
        sut.push(5)
        assertEqual(l..(sut), 1)
        assertEqual(sut.head().value(), 5)

    ___ test_can_pop_from_non_empty_list
        sut LinkedList([3, 4, 5])
        assertEqual(sut.p.. ), 5)
        assertEqual(l..(sut), 2)
        assertEqual(sut.head().value(), 4)

    ___ test_pop_from_singleton_list_removes_head
        sut LinkedList([1])
        assertEqual(sut.p.. ), 1)
        w__ assertRaisesWithMessage(EmptyListException
            sut.head()

    ___ test_error_on_empty_list_pop
        sut LinkedList()
        w__ assertRaisesWithMessage(EmptyListException
            sut.p.. )

    ___ test_push_and_pop
        sut LinkedList([1, 2])
        sut.push(3)
        assertEqual(l..(sut), 3)
        assertEqual(sut.p.. ), 3)
        assertEqual(sut.p.. ), 2)
        assertEqual(sut.p.. ), 1)
        assertEqual(l..(sut), 0)
        sut.push(4)
        assertEqual(l..(sut), 1)
        assertEqual(sut.head().value(), 4)

    ___ test_singleton_list_head_has_no_next
        sut LinkedList([1])
        assertIsNone(sut.head().next

    ___ test_non_empty_list_traverse
        sut LinkedList(r..(10
        current sut.head()
        ___ i __ r..(10
            assertEqual(current.value(), 9 - i)
            current current.next()
        assertIsNone(current)

    ___ test_empty_linked_list_to_list_is_empty
        sut LinkedList()
        assertEqual(l..(sut), [])

    ___ test_singleton_linked_list_to_list_list_with_singular_element
        sut LinkedList([1])
        assertEqual(l..(sut), [1])

    ___ test_non_empty_linked_list_to_list_is_list_with_all_elements
        sut LinkedList([1, 2, 3])
        assertEqual(l..(sut), [3, 2, 1])

    ___ test_reversed_empty_list_is_empty_list
        sut LinkedList([])
        assertEqual(l..(sut.r.., [])

    ___ test_reversed_singleton_list_is_same_list
        sut LinkedList([1])
        assertEqual(l..(sut.r.., [1])

    ___ test_reverse_non_empty_list
        sut LinkedList([1, 2, 3])
        assertEqual(l..(sut.r.., [1, 2, 3])

    # Utility functions
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
