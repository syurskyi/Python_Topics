# ch9/example1.py

____ ma__ ______ sqrt
____ t_i_ ______ d_t_ as timer

___ is_prime(x):
    print('Processing %i...' % x)

    __ x < 2:
        print('%i is not a prime number.' % x)

    ____ x __ 2:
        print('%i is a prime number.' % x)

    ____ x % 2 __ 0:
        print('%i is not a prime number.' % x)

    ____
        limit _ int(sqrt(x)) + 1
        ___ i __ ra..(3, limit, 2):
            __ x % i __ 0:
                print('%i is not a prime number.' % x)
                r_

        print('%i is a prime number.' % x)

__ _______ __ _______

    start _ timer()
    is_prime(9637529763296797)
    is_prime(427920331)
    is_prime(157)
    print('Took %.2f seconds.' % (timer() - start))
