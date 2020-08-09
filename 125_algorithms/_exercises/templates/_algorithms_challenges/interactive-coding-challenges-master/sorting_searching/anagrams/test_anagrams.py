from nose.tools ______ assert_equal, assert_raises


class TestAnagrams(object

    ___ test_group_anagrams(self
        anagram = Anagram()
        assert_raises(TypeError, anagram.group_anagrams, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        assert_equal(anagram.group_anagrams(data), expected)

        print('Success: test_group_anagrams')


___ main(
    test = TestAnagrams()
    test.test_group_anagrams()


__ __name__ __ '__main__':
    main()