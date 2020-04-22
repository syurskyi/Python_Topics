# ch6/example1.py

____ m.. ______ Process
______ ti..


___ count_down(name, delay):
    print('Process %s starting...' % name)

    counter _ 5

    w__ counter:
        t__.s..(delay)
        print('Process %s counting down: %i...' % (name, counter))
        counter -_ 1

    print('Process %s exiting...' % name)


__ _______ __ _______
    process1 _ P..(target_count_down, args_('A', 0.5))
    process2 _ P..(target_count_down, args_('B', 0.5))

    process1.s..
    process2.s..

    process1.j..
    process2.j..

    print('Done.')
