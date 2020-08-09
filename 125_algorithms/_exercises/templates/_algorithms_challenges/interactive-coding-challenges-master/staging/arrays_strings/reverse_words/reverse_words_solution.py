from nose.tools ______ assert_equal

class UnitTest (object
    ___ testReverseWords(self, func
            assert_equal(func('the sun is hot'), 'eht nus si toh')
            assert_equal(func(''), None)
            assert_equal(func('123 456 789'), '321 654 987')
            assert_equal(func('magic'), 'cigam')
            print('Success: reverse_words')
            
___ main(
    test = UnitTest()
    test.testReverseWords(reverse_words)

__ __name____"__main__":
  main()