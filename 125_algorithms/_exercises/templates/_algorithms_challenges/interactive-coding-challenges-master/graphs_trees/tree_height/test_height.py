from nose.tools ______ assert_equal


class TestHeight(object

    ___ test_height(self
        bst = BstHeight(Node(5))
        assert_equal(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        assert_equal(bst.height(bst.root), 3)

        print('Success: test_height')


___ main(
    test = TestHeight()
    test.test_height()


__ __name__ __ '__main__':
    main()