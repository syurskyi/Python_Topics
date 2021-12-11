# spinner_async_experiment.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

______ _
______ i__

______ primes

@ ___ spin(msg: s..)  N..:
    ___ char __ i__.c..(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=T.., end='')
        ___
            await _.s..(.1)
        _____ _.CancelledError:
            ____
    print('THIS WILL NEVER BE OUTPUT')

@ ___ check(n: in.)  in.:
    r_ primes.is_prime(n)  # <4>

@ ___ supervisor(n: in.)  in.:
    spinner = _.create_task(spin('thinking!'))  # <1>
    print('spinner object:', spinner)  # <2>
    result = await check(n)  # <3>
    spinner.cancel()  # <5>
    r_ result
# end::SPINNER_ASYNC_EXPERIMENT[]

___ main()  N..:
    n = 5_000_111_000_222_021
    result = _.run(supervisor(n))
    msg = 'is' __ result else 'is not'
    print(f'{n:,} {msg} prime')

__ _____ __ ______
    main()
