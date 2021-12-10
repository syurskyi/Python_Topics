# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_THREAD_TOP[]
______ i__
______ t__
from _ ______ ?, Event

___ spin(msg: s.., done: Event)  N..:  # <1>
    ___ char __ i__.c..(r'\|/-'):  # <2>
        status = f'\r{char} {msg}'  # <3>
        print(status, end='', flush=T..)
        __ done.wait(.1):  # <4>
            ____  # <5>
    blanks = ' ' * l..(status)
    print(f'\r{blanks}\r', end='')  # <6>

___ slow()  in.:
    t__.s..(3)  # <7>
    r_ 42
# end::SPINNER_THREAD_TOP[]

# tag::SPINNER_THREAD_REST[]
___ supervisor()  in.:  # <1>
    done = Event()  # <2>
    spinner = ? ?_spin,  ?_('thinking!', done))  # <3>
    print(f'spinner object: {spinner}')  # <4>
    spinner.s..  # <5>
    result = slow()  # <6>
    done.set()  # <7>
    spinner.j..  # <8>
    r_ result

___ main()  N..:
    result = supervisor()  # <9>
    print(f'Answer: {result}')

__ _____ __ ______
    main()
# end::SPINNER_THREAD_REST[]
