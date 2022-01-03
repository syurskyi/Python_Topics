_______ unittest

____ custom_set _______ CustomSet


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

c_ CustomSetTest(unittest.TestCase):
    ___ test_sets_with_no_elements_are_empty
        sut = CustomSet()
        assertIs(sut.isempty(), T..)

    ___ test_sets_with_elements_are_not_empty
        sut = CustomSet([1])
        assertIs(sut.isempty(), F..)

    ___ test_empty_set_contains_nothing
        sut = CustomSet()
        assertNotIn(1, sut)

    ___ test_set_contains_when_element_in_set
        sut = CustomSet([1])
        assertIn(1, sut)

    ___ test_set_does_not_contains_when_element_not_in_set
        sut = CustomSet([1, 2, 3])
        assertNotIn(4, sut)

    ___ test_empty_set_is_subset_of_another_empty_set
        set1 = CustomSet()
        set2 = CustomSet()
        assertIs(set1.issubset(set2), T..)

    ___ test_empty_set_is_subset_of_non_empty_set
        set1 = CustomSet()
        set2 = CustomSet([1])
        assertIs(set1.issubset(set2), T..)

    ___ test_non_empty_set_is_not_subet_of_empty_set
        set1 = CustomSet([1])
        set2 = CustomSet()
        assertIs(set1.issubset(set2), F..)

    ___ test_set_is_subset_of_set_with_exact_same_elements
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 3])
        assertIs(set1.issubset(set2), T..)

    ___ test_set_is_subset_of_larger_set_with_same_elements
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 1, 2, 3])
        assertIs(set1.issubset(set2), T..)

    ___ test_set_not_subset_of_set_that_does_not_contain_its_elements
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 1, 3])
        assertIs(set1.issubset(set2), F..)

    ___ test_empty_set_disjoint_with_itself
        set1 = CustomSet()
        set2 = CustomSet()
        assertIs(set1.isdisjoint(set2), T..)

    ___ test_empty_set_disjoint_with_non_empty_set
        set1 = CustomSet()
        set2 = CustomSet([1])
        assertIs(set1.isdisjoint(set2), T..)

    ___ test_non_empty_set_disjoint_with_empty_set
        set1 = CustomSet([1])
        set2 = CustomSet()
        assertIs(set1.isdisjoint(set2), T..)

    ___ test_sets_not_disjoint_if_element_is_shared
        set1 = CustomSet([1, 2])
        set2 = CustomSet([2, 3])
        assertIs(set1.isdisjoint(set2), F..)

    ___ test_sets_disjoint_if_not_elements_are_shared
        set1 = CustomSet([1, 2])
        set2 = CustomSet([3, 4])
        assertIs(set1.isdisjoint(set2), T..)

    ___ test_empty_sets_are_equal
        set1 = CustomSet()
        set2 = CustomSet()
        assertEqual(set1, set2)

    ___ test_empty_set_not_equal_to_non_empty_set
        set1 = CustomSet()
        set2 = CustomSet([1, 2, 3])
        assertNotEqual(set1, set2)

    ___ test_non_empty_set_not_equal_to_empty_set
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet()
        assertNotEqual(set1, set2)

    ___ test_sets_with_same_exact_same_elements_are_equal
        set1 = CustomSet([1, 2])
        set2 = CustomSet([2, 1])
        assertEqual(set1, set2)

    ___ test_sets_with_different_elements_are_not_equal
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 4])
        assertNotEqual(set1, set2)

    ___ test_set_is_not_equal_to_larger_set_with_same_elements
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 3, 4])
        assertNotEqual(set1, set2)

    ___ test_add_to_empty_set
        sut = CustomSet()
        sut.add(1)
        expected = CustomSet([1])
        assertEqual(sut, expected)

    ___ test_add_to_non_empty_set
        sut = CustomSet([1, 2, 4])
        sut.add(3)
        expected = CustomSet([1, 2, 3, 4])
        assertEqual(sut, expected)

    ___ test_adding_existing_element_does_not_change_set
        sut = CustomSet([1, 2, 3])
        sut.add(3)
        expected = CustomSet([1, 2, 3])
        assertEqual(sut, expected)

    ___ test_intersection_of_two_empty_sets_is_empty_set
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        assertEqual(set1.intersection(set2), expected)

    ___ test_intersection_of_empty_set_and_non_empty_set_is_empty_set
        set1 = CustomSet()
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet()
        assertEqual(set1.intersection(set2), expected)

    ___ test_intersection_of_non_empty_set_and_empty_set_is_empty_set
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet()
        expected = CustomSet()
        assertEqual(set1.intersection(set2), expected)

    ___ test_intersection_of_sets_with_no_shared_elements_is_empty_set
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 5, 6])
        expected = CustomSet()
        assertEqual(set1.intersection(set2), expected)

    ___ test_intersection_contains_shared_elements_only
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet([2, 3])
        assertEqual(set1.intersection(set2), expected)

    ___ test_difference_of_two_empty_sets_is_empty_set
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        assertEqual(set1 - set2, expected)

    ___ test_difference_of_empty_set_and_non_empty_set_is_empty_set
        set1 = CustomSet()
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet()
        assertEqual(set1 - set2, expected)

    ___ test_difference_of_non_empty_set_and_empty_set_is_non_empty_set
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet()
        expected = CustomSet([1, 2, 3, 4])
        assertEqual(set1 - set2, expected)

    ___ test_difference_of_non_empty_sets_elements_in_first_set_only
        set1 = CustomSet([3, 2, 1])
        set2 = CustomSet([2, 4])
        expected = CustomSet([1, 3])
        assertEqual(set1 - set2, expected)

    ___ test_union_of_empty_sets_is_empty_set
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        assertEqual(set1 + set2, expected)

    ___ test_union_of_empty_set_and_non_empty_set_is_the_non_empty_set
        set1 = CustomSet()
        set2 = CustomSet([2])
        expected = CustomSet([2])
        assertEqual(set1 + set2, expected)

    ___ test_union_of_non_empty_set_and_empty_set_is_the_non_empty_set
        set1 = CustomSet([1, 3])
        set2 = CustomSet()
        expected = CustomSet([1, 3])
        assertEqual(set1 + set2, expected)

    ___ test_union_of_non_empty_sets_contains_all_unique_elements
        set1 = CustomSet([1, 3])
        set2 = CustomSet([2, 3])
        expected = CustomSet([1, 2, 3])
        assertEqual(set1 + set2, expected)


__ __name__ __ '__main__':
    unittest.main()
