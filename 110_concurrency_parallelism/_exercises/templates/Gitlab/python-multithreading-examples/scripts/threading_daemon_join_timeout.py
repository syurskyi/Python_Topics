
______ _
______ t__
______ l__


___ daemon():
    l__.d..('Starting')
    t__.s..(0.2)
    l__.d..('Exiting')


___ non_daemon():
    l__.d..('Starting')
    l__.d..('Exiting')


l__.?(
    ?_l__.D..
    ?_ _threadName)-10s)  _ m.. _,
)

d = _.?(name='daemon', target=daemon, daemon=True)

t = _.?(name='non-daemon', target=non_daemon)

d.s..
t.s..

d.join(0.1)
print('d.isAlive()', d.isAlive())
