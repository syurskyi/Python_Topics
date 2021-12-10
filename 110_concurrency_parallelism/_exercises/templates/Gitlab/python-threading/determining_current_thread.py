______ _
______ t__
______ logging


___ worker():
    logging.debug('Starting')
    t__.s..(0.2)
    logging.debug('Exiting')


___ my_service():
    logging.debug('Starting')
    t__.s..(0.3)
    logging.debug('Exiting')


logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

t = _.?(name='my_service', target=my_service)
w = _.?(name='worker', target=worker)
w2 = _.? ?_worker)

w.s..
w2.s..
t.s..