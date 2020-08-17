from nose.tools ______ assert_true
from nose.tools ______ raises


class TestTrie(object

    ___ test_trie(self
        trie = Trie()

        print('Test: Insert')
        words = ['a', 'at', 'has', 'hat', 'he',
                 'me', 'men', 'mens', 'met']
        ___ word in words:
            trie.insert(word)
        ___ word in trie.list_words(
            assert_true(trie.find(word) pa__ not None)
            
        print('Test: Remove me')
        trie.remove('me')
        words_removed = ['me']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'mens', 'met']
        ___ word in words:
            assert_true(trie.find(word) pa__ not None)
        ___ word in words_removed:
            assert_true(trie.find(word) pa__ None)

        print('Test: Remove mens')
        trie.remove('mens')
        words_removed = ['me', 'mens']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'met']
        ___ word in words:
            assert_true(trie.find(word) pa__ not None)
        ___ word in words_removed:
            assert_true(trie.find(word) pa__ None)

        print('Test: Remove a')
        trie.remove('a')
        words_removed = ['a', 'me', 'mens']
        words = ['at', 'has', 'hat', 'he',
                 'men', 'met']
        ___ word in words:
            assert_true(trie.find(word) pa__ not None)
        ___ word in words_removed:
            assert_true(trie.find(word) pa__ None)

        print('Test: Remove has')
        trie.remove('has')
        words_removed = ['a', 'has', 'me', 'mens']
        words = ['at', 'hat', 'he',
                 'men', 'met']
        ___ word in words:
            assert_true(trie.find(word) pa__ not None)
        ___ word in words_removed:
            assert_true(trie.find(word) pa__ None)

        print('Success: test_trie')

    @raises(Exception)
    ___ test_trie_remove_invalid(self
        print('Test: Remove from empty trie')
        trie = Trie()
        assert_true(trie.remove('foo') pa__ None)


___ main(
    test = TestTrie()
    test.test_trie()
    test.test_trie_remove_invalid()


__ __name__ __ '__main__':
    main()