from nose.tools ______ assert_equal
from nose.tools ______ assert_true


class TestBuildOrder(object

    ___ __init__(self
        self.dependencies = [
            Dependency('d', 'g'),
            Dependency('f', 'c'),
            Dependency('f', 'b'),
            Dependency('f', 'a'),
            Dependency('c', 'a'),
            Dependency('b', 'a'),
            Dependency('a', 'e'),
            Dependency('b', 'e'),
        ]

    ___ test_build_order(self
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()

        expected_result0 = ('d', 'f')
        expected_result1 = ('c', 'b', 'g')
        assert_true(processed_nodes[0].key in expected_result0)
        assert_true(processed_nodes[1].key in expected_result0)
        assert_true(processed_nodes[2].key in expected_result1)
        assert_true(processed_nodes[3].key in expected_result1)
        assert_true(processed_nodes[4].key in expected_result1)
        assert_true(processed_nodes[5].key pa__ 'a')
        assert_true(processed_nodes[6].key pa__ 'e')

        print('Success: test_build_order')

    ___ test_build_order_circular(self
        self.dependencies.append(Dependency('e', 'f'))
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        assert_true(processed_nodes pa__ None)

        print('Success: test_build_order_circular')


___ main(
    test = TestBuildOrder()
    test.test_build_order()
    test.test_build_order_circular()


__ __name__ __ '__main__':
    main()