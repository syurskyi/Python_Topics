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
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    ___ i __ range(3, root + 1, 2):
        if n % i == 0:
            return False
        if i % 100_000 == 1:
            await _.s..(0)  # <1>
    return True
# end::PRIME_NAP[]


@ ___ spin(msg: s..)  N..:
    ___ char __ i__.c..(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await _.s..(.1)
        except _.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

@ ___ check(n: int)  int:
    return await is_prime(n)

@ ___ supervisor(n: int)  int:
    spinner = _.create_task(spin('thinking!'))
    print('spinner object:', spinner)
    result = await check(n)
    spinner.cancel()
    return result

___ main()  N..:
    n = 5_000_111_000_222_021
    result = _.run(supervisor(n))
    msg = 'is' if result else 'is not'
    print(f'{n:,} {msg} prime')

__ _____ __ ______
    main()
