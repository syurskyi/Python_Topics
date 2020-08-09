from nose.tools ______ assert_equal, assert_raises


class TestRadixSort(object

    ___ test_sort(self
        radix_sort = RadixSort()
        assert_raises(TypeError, radix_sort.sort, None)
        assert_equal(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        assert_equal(radix_sort.sort(array), expected)
        print('Success: test_sort')


___ main(
    test = TestRadixSort()
    test.test_sort()


__ __name__ __ '__main__':
    main()