# spinner_async.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_ASYNC_TOP[]
______ _
______ i__

@ ___ spin msg s..  N..  # <1>
    ___ char __ i__.c.. _ \|/-
        status = f'\r{char} {msg}'
        print ? flush=T.., end='')
        ___
            await _.s..(.1)  # <2>
        except _.CancelledError:  # <3>
            ____
    blanks = ' ' * l..(status)
    print(f'\r{blanks}\r', end='')

@ ___ slow()  in.:
    await _.s..(3)  # <4>
    r_ 42
# end::SPINNER_ASYNC_TOP[]

# tag::SPINNER_ASYNC_START[]
___ main()  N..:  # <1>
    result = _.run(supervisor())  # <2>
    print(f'Answer: {result}')

@ ___ supervisor()  in.:  # <3>
    spinner = _.create_task(spin('thinking!'))  # <4>
    print(f'spinner object: {spinner}')  # <5>
    result = await slow()  # <6>
    spinner.cancel()  # <7>
    r_ result

__ _____ __ ______
    main()
# end::SPINNER_ASYNC_START[]
