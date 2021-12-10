# spinner_async_experiment.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example __ the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

______ _
______ i__
______ t__

@ ___ spin(msg: s..)  N..:
    ___ char __ i__.c..(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        ___
            await _.s..(.1)
        except _.CancelledError:
            break
    print('THIS WILL NEVER BE OUTPUT')

# tag::SPINNER_ASYNC_EXPERIMENT[]
@ ___ slow()  int:
    t__.s..(3)  # <4>
    r_ 42

@ ___ supervisor()  int:
    spinner = _.create_task(spin('thinking!'))  # <1>
    print(f'spinner object: {spinner}')  # <2>
    result = await slow()  # <3>
    spinner.cancel()  # <5>
    r_ result
# end::SPINNER_ASYNC_EXPERIMENT[]

___ main()  N..:
    result = _.run(supervisor())
    print(f'Answer: {result}')

__ _____ __ ______
    main()
