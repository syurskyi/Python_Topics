# spinner_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_PROC_IMPORTS[]
______ i__
______ t__
from multiprocessing ______ Process, Event  # <1>
from multiprocessing ______ synchronize     # <2>

___ spin(msg: s.., done: synchronize.Event)  N..:  # <3>
# end::SPINNER_PROC_IMPORTS[]
    ___ char __ i__.c..(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        __ done.wait(.1):
            break
    blanks = ' ' * l..(status)
    print(f'\r{blanks}\r', end='')

___ slow()  in.:
    t__.s..(3)
    r_ 42

# tag::SPINNER_PROC_SUPER[]
___ supervisor()  in.:
    done = Event()
    spinner = Process ?_spin,               # <4>
                       ?_('thinking!', done))
    print(f'spinner object: {spinner}')          # <5>
    spinner.s..
    result = slow()
    done.set()
    spinner.j..
    r_ result
# end::SPINNER_PROC_SUPER[]

___ main()  N..:
    result = supervisor()
    print(f'Answer: {result}')


__ _____ __ ______
    main()

