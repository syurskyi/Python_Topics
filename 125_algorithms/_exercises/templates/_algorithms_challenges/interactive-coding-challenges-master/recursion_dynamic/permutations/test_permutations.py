from nose.tools ______ assert_equal


class TestPermutations(object

    ___ test_permutations(self
        permutations = Permutations()
        assert_equal(permutations.find_permutations(None), None)
        assert_equal(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        assert_equal(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


___ main(
    test = TestPermutations()
    test.test_permutations()


__ __name__ __ '__main__':
    main()