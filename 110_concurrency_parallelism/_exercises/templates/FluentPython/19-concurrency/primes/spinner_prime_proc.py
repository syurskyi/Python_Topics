# spinner_prime_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

______ i__
____ multiprocessing ______ Process, Event
____ multiprocessing ______ synchronize

____ primes ______ is_prime

___ spin(msg: s.., done: synchronize.Event)  N..:  # <1>
    ___ char __ i__.c..(r'\|/-'):  # <2>
        status = f'\r{char} {msg}'  # <3>
        print(status, end='', flush=T..)
        __ done.w..(.1):  # <4>
            ____  # <5>
    blanks = ' ' * l..(status)
    print(f'\r{blanks}\r', end='')  # <6>

___ check(n: in.)  in.:
    r_ is_prime(n)

___ supervisor(n: in.)  in.:  # <1>
    done = Event()  # <2>
    spinner = Process ?_spin,
                       ?_('thinking!', done))  # <3>
    print(f'spinner object: {spinner}')  # <4>
    spinner.s..  # <5>
    result = check(n)  # <6>
    done.set()  # <7>
    spinner.j..  # <8>
    r_ result

___ main()  N..:
    n = 5_000_111_000_222_021
    result = supervisor(n)  # <9>
    msg = 'is' __ result else 'is not'
    print(f'{n:,} {msg} prime')

__ _____ __ ______
    main()
