from nose.tools ______ assert_equal


class TestBfs(object

    ___ __init__(self
        self.results = Results()

    ___ test_bfs(self
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        assert_equal(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


___ main(
    test = TestBfs()
    test.test_bfs()


__ __name__ __ '__main__':
    main()