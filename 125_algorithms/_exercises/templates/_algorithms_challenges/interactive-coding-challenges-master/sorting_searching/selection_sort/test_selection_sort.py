from nose.tools ______ assert_equal, assert_raises


class TestSelectionSort(object

    ___ test_selection_sort(self, func
        print('None input')
        assert_raises(TypeError, func, None)

        print('Empty input')
        assert_equal(func([]), [])

        print('One element')
        assert_equal(func([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        assert_equal(func(data), sorted(data))

        print('Success: test_selection_sort\n')


___ main(
    test = TestSelectionSort()
    selection_sort = SelectionSort()
    test.test_selection_sort(selection_sort.sort)
    try:
        test.test_selection_sort(selection_sort.sort_recursive)
        test.test_selection_sort(selection_sort.sor_iterative_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


__ __name__ __ '__main__':
    main()