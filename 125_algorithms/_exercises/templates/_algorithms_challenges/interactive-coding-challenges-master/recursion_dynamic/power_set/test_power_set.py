from nose.tools ______ assert_equal


class TestPowerSet(object

    ___ test_power_set(self
        input_set = ''
        expected = ['']
        self.run_test(input_set, expected)
        input_set = 'a'
        expected = ['a', '']
        self.run_test(input_set, expected)
        input_set = 'ab'
        expected = ['a', 'ab', 'b', '']
        self.run_test(input_set, expected)
        input_set = 'abc'
        expected = ['a', 'ab', 'abc', 'ac',
                    'b', 'bc', 'c', '']
        self.run_test(input_set, expected)
        input_set = 'aabc'
        expected = ['a', 'aa', 'aab', 'aabc', 
                    'aac', 'ab', 'abc', 'ac', 
                    'b', 'bc', 'c', '']
        self.run_test(input_set, expected)
        print('Success: test_power_set')

    ___ run_test(self, input_set, expected
        combinatoric = Combinatoric()
        result = combinatoric.find_power_set(input_set)
        assert_equal(result, expected)


___ main(
    test = TestPowerSet()
    test.test_power_set()


__  -n __ '__main__':
    main()