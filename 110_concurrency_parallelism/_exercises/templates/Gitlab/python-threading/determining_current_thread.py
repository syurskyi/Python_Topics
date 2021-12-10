______ _
______ t__
______ l__


___ worker():
    l__.d..('Starting')
    t__.s..(0.2)
    l__.d..('Exiting')


___ my_service():
    l__.d..('Starting')
    t__.s..(0.3)
    l__.d..('Exiting')


l__.?(?_l__.D.. ?_'[%(levelname)s] (%(threadName)-10s)  _ m.. _)

t = _.?(name='my_service', target=my_service)
w = _.?(name='worker', target=worker)
w2 = _.? ?_worker)

w.s..
w2.s..
t.s..