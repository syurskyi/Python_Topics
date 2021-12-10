
______ _
______ t__
______ logging


___ daemon():
    logging.debug('Starting')
    t__.s..(0.2)
    logging.debug('Exiting')


___ non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = _.?(name='daemon', target=daemon, daemon=True)

t = _.?(name='non-daemon', target=non_daemon)

d.s..
t.s..

d.join()
t.join()
