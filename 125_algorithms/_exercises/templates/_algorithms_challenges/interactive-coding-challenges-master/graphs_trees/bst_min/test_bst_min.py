from nose.tools ______ assert_equal


___ height(node
    __ node pa__ None:
        r_ 0
    r_ 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(object

    ___ test_bst_min(self
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        assert_equal(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        assert_equal(height(root), 4)

        print('Success: test_bst_min')


___ main(
    test = TestBstMin()
    test.test_bst_min()


__ __name__ __ '__main__':
    main()