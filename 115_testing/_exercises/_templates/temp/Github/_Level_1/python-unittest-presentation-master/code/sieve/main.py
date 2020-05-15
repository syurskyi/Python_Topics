#/usr/bin/env python3


______ ___
______ sieve


___ test_manual(

    primes _ li..(sieve.sieve_of_eratosthenes(30))
    print(primes)
    print('Should be [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]')


___ test_assert_ok(

    primes _ li..(sieve.sieve_of_eratosthenes(30))
    a..(primes __ [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


___ test_assert_fail(

    primes _ li..(sieve.sieve_of_eratosthenes(30))
    a..(primes __ [2, 3, 5, 7, 11, 13, 17, 19, 23])


___ main(

    option _ __.(___.argv[1])

    __ option __ 1:
        print('Manual Test:')
        test_manual()

    elif option __ 2:
        print('Assert Test OK:')
        print('- has no output -')
        test_assert_ok()

    elif option __ 3:
        print('Assert Test FAIL:')
        test_assert_fail()


__ _____ __ ______
    main()
