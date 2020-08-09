from nose.tools ______ assert_equal, assert_raises


class TestRansomNote(object

    ___ test_ransom_note(self
        solution = Solution()
        assert_raises(TypeError, solution.match_note_to_magazine, None, None)
        assert_equal(solution.match_note_to_magazine('', ''), True)
        assert_equal(solution.match_note_to_magazine('a', 'b'), False)
        assert_equal(solution.match_note_to_magazine('aa', 'ab'), False)
        assert_equal(solution.match_note_to_magazine('aa', 'aab'), True)
        print('Success: test_ransom_note')


___ main(
    test = TestRansomNote()
    test.test_ransom_note()


__ __name__ __ '__main__':
    main()