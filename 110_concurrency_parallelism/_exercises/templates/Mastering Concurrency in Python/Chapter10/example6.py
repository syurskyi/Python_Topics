# ch10/example6.py

____ ma__ ______ sqrt
______ a..
____ c__.f.. ______ PPE..
____ t_i_ ______ d_t_ as timer

#async def is_prime(x):
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

? ___ main():

    task1 _ loop.run_in_executor(executor, is_prime, 9637529763296797)
    task2 _ loop.run_in_executor(executor, is_prime, 427920331)
    task3 _ loop.run_in_executor(executor, is_prime, 157)

    await ?.gather(*[task1, task2, task3])

__ _______ __ _______
    ___
        start _ timer()

        executor _ PPE..(max_workers_3)
        loop _ ?.g_e_l..
        loop.r_u_c..(main())

        print('Took %.2f seconds.' % (timer() - start))

    ______ E.. as e:
        print('There was a problem:')
        print(st.(e))

    f..
        loop.close()
