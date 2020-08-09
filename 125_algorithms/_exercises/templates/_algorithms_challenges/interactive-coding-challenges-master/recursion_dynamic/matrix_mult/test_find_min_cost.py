from nose.tools ______ assert_equal, assert_raises


class TestMatrixMultiplicationCost(object

    ___ test_find_min_cost(self
        matrix_mult_cost = MatrixMultiplicationCost()
        assert_raises(TypeError, matrix_mult_cost.find_min_cost, None)
        assert_equal(matrix_mult_cost.find_min_cost([]), 0)
        matrices = [Matrix(2, 3),
                    Matrix(3, 6),
                    Matrix(6, 4),
                    Matrix(4, 5)]
        expected_cost = 124
        assert_equal(matrix_mult_cost.find_min_cost(matrices), expected_cost)
        print('Success: test_find_min_cost')


___ main(
    test = TestMatrixMultiplicationCost()
    test.test_find_min_cost()


__ __name__ __ '__main__':
    main()