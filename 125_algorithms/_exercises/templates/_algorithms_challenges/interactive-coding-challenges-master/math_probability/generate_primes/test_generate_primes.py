from nose.tools ______ assert_equal, assert_raises


class TestMath(object

    ___ test_generate_primes(self
        prime_generator = PrimeGenerator()
        assert_raises(TypeError, prime_generator.generate_primes, None)
        assert_raises(TypeError, prime_generator.generate_primes, 98.6)
        assert_equal(prime_generator.generate_primes(20), [False, False, True, 
                                                           True, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True])
        print('Success: generate_primes')


___ main(
    test = TestMath()
    test.test_generate_primes()


__ __name__ __ '__main__':
    main()