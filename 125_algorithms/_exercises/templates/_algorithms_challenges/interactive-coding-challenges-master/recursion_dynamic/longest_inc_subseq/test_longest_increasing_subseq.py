from nose.tools ______ assert_equal, assert_raises


class TestLongestIncreasingSubseq(object

    ___ test_longest_increasing_subseq(self
        subseq = Subsequence()
        assert_raises(TypeError, subseq.longest_inc_subseq, None)
        assert_equal(subseq.longest_inc_subseq([]), [])
        seq = [3, 4, -1, 0, 6, 2, 3]
        expected = [-1, 0, 2, 3]
        assert_equal(subseq.longest_inc_subseq(seq), expected)
        print('Success: test_longest_increasing_subseq')


___ main(
    test = TestLongestIncreasingSubseq()
    test.test_longest_increasing_subseq()


__ __name__ __ '__main__':
    main()