from nose.tools ______ assert_equal, assert_raises


class TestInsertionSort(object

    ___ test_insertion_sort(self
        insertion_sort = InsertionSort()

        print('None input')
        assert_raises(TypeError, insertion_sort.sort, None)

        print('Empty input')
        assert_equal(insertion_sort.sort([]), [])

        print('One element')
        assert_equal(insertion_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(insertion_sort.sort(data), sorted(data))

        print('Success: test_insertion_sort')


___ main(
    test = TestInsertionSort()
    test.test_insertion_sort()


__ __name__ __ '__main__':
    main()