# ch6/example2.py

____ m.. ______ Process, current_process
______ ti..


___ f1():
    pname _ current_process().name
    print('Starting process %s...' % pname)
    t__.s..(2)
    print('Exiting process %s...' % pname)

___ f2():
    pname _ current_process().name
    print('Starting process %s...' % pname)
    t__.s..(4)
    print('Exiting process %s...' % pname)


__ _______ __ _______
    p1 _ P..(name_'Worker 1', target_f1)
    p2 _ P..(name_'Worker 2', target_f2)
    p3 _ P..(target_f1)

    p1.s..
    p2.s..
    p3.s..

    p1.j..
    p2.j..
    p3.j..
