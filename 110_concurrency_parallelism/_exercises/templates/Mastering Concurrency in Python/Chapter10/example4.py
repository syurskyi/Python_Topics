# ch9/example1.py

____ ma__ ______ sqrt
______ a..
____ t_i_ ______ d_t_ as timer

? ___ is_prime(x):
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
            ____ i % 100000 __ 1:
                await ?.s..(0)

        print('%i is a prime number.' % x)

? ___ main():

    task1 _ loop.create_task(is_prime(9637529763296797))
    task2 _ loop.create_task(is_prime(427920331))
    task3 _ loop.create_task(is_prime(157))

    await ?.wait([task1, task2, task3])

__ _______ __ _______
    ___
        start _ timer()
        loop _ ?.get_event_loop()
        loop.run_until_complete(main())
        print('Took %.2f seconds.' % (timer() - start))
    ______ Exception as e:
        print('There was a problem:')
        print(st.(e))
    f..
        loop.close()
