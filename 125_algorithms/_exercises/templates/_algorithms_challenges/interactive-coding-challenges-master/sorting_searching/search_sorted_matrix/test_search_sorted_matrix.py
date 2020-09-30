from nose.tools ______ assert_equal, assert_raises


class TestSortedMatrix(object

    ___ test_find_val(self
        matrix = [[20, 40, 63, 80],
                  [30, 50, 80, 90],
                  [40, 60, 110, 110],
                  [50, 65, 105, 150]]
        sorted_matrix = SortedMatrix()
        assert_raises(TypeError, sorted_matrix.find_val, None, None)
        assert_equal(sorted_matrix.find_val(matrix, 1000), None)
        assert_equal(sorted_matrix.find_val(matrix, 60), (2, 1))
        print('Success: test_find_val')


___ main(
    test = TestSortedMatrix()
    test.test_find_val()


__  -n __ '__main__':
    main()