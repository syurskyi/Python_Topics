from nose.tools ______ assert_equal, assert_raises


class TestIslandPerimeter(object

    ___ test_island_perimeter(self
        solution = Solution()
        assert_raises(TypeError, solution.island_perimeter, None)
        data = [[1, 0]]
        expected = 4
        assert_equal(solution.island_perimeter(data), expected)
        data = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]
        expected = 16
        assert_equal(solution.island_perimeter(data), expected)
        print('Success: test_island_perimeter')


___ main(
    test = TestIslandPerimeter()
    test.test_island_perimeter()


__ __name__ __ '__main__':
    main()