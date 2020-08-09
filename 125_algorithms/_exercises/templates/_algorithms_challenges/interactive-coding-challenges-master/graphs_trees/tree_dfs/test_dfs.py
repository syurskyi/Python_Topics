from nose.tools ______ assert_equal


class TestDfs(object

    ___ __init__(self
        self.results = Results()

    ___ test_dfs(self
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        bst.in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


___ main(
    test = TestDfs()
    test.test_dfs()


__ __name__ __ '__main__':
    main()