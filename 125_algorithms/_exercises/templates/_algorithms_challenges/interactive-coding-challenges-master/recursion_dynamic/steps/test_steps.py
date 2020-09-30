from nose.tools ______ assert_equal, assert_raises


class TestSteps(object

    ___ test_steps(self
        steps = Steps()
        assert_raises(TypeError, steps.count_ways, None)
        assert_raises(TypeError, steps.count_ways, -1)
        assert_equal(steps.count_ways(0), 1)
        assert_equal(steps.count_ways(1), 1)
        assert_equal(steps.count_ways(2), 2)
        assert_equal(steps.count_ways(3), 4)
        assert_equal(steps.count_ways(4), 7)
        assert_equal(steps.count_ways(10), 274)
        print('Success: test_steps')


___ main(
    test = TestSteps()
    test.test_steps()


__  -n __ '__main__':
    main()