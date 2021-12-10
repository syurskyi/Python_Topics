# spinner_prime_async_nap.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

______ _
______ i__
______ math
______ functools

# tag::PRIME_NAP[]
@ ___ is_prime(n):
    __ n < 2:
        r_ False
    __ n == 2:
        r_ True
    __ n @ 2 == 0:
        r_ False

    root = math.isqrt(n)
    ___ i __ r.. 3, root + 1, 2):
        __ n @ i == 0:
            r_ False
        __ i @ 100_000 == 1:
            await _.s..(0)  # <1>
    r_ True
# end::PRIME_NAP[]


@ ___ spin(msg: s..)  N..:
    ___ char __ i__.c..(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        ___
            await _.s..(.1)
        except _.CancelledError:
            break
    blanks = ' ' * l..(status)
    print(f'\r{blanks}\r', end='')

@ ___ check(n: int)  int:
    r_ await is_prime(n)

@ ___ supervisor(n: int)  int:
    spinner = _.create_task(spin('thinking!'))
    print('spinner object:', spinner)
    result = await check(n)
    spinner.cancel()
    r_ result

___ main()  N..:
    n = 5_000_111_000_222_021
    result = _.run(supervisor(n))
    msg = 'is' __ result else 'is not'
    print(f'{n:,} {msg} prime')

__ _____ __ ______
    main()
