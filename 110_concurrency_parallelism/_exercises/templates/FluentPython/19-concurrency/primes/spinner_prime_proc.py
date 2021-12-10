# spinner_prime_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

______ i__
from multiprocessing ______ Process, Event
from multiprocessing ______ synchronize

from primes ______ is_prime

___ spin(msg: s.., done: synchronize.Event)  N..:  # <1>
    ___ char __ i__.c..(r'\|/-'):  # <2>
        status = f'\r{char} {msg}'  # <3>
        print(status, end='', flush=True)
        if done.wait(.1):  # <4>
            break  # <5>
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')  # <6>

___ check(n: int)  int:
    return is_prime(n)

___ supervisor(n: int)  int:  # <1>
    done = Event()  # <2>
    spinner = Process ?_spin,
                       ?_('thinking!', done))  # <3>
    print(f'spinner object: {spinner}')  # <4>
    spinner.s..  # <5>
    result = check(n)  # <6>
    done.set()  # <7>
    spinner.join()  # <8>
    return result

___ main()  N..:
    n = 5_000_111_000_222_021
    result = supervisor(n)  # <9>
    msg = 'is' if result else 'is not'
    print(f'{n:,} {msg} prime')

__ _____ __ ______
    main()
