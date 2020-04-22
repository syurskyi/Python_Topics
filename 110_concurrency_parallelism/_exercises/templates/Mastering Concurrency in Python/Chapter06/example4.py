# ch6/example4.py

____ m.. ______ Process, current_process
______ ti..


___ f1():
    p _ current_process()
    print('Starting process %s, ID %s...' % (p.name, p.pid))
    t__.s..(4)
    print('Exiting process %s, ID %s...' % (p.name, p.pid))

___ f2():
    p _ current_process()
    print('Starting process %s, ID %s...' % (p.name, p.pid))
    t__.s..(2)
    print('Exiting process %s, ID %s...' % (p.name, p.pid))


__ _______ __ _______
    p1 _ P..(name_'Worker 1', target_f1)
    p1.daemon _ T..
    p2 _ P..(name_'Worker 2', target_f2)

    p1.s..
    t__.s..(1)
    p2.s..
