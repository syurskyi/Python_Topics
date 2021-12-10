______ _
______ t__
______ logging


___ delayed():
    logging.debug('worker running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

t1 = _.Timer(0.3, delayed)
t1.setName('t1')
t2 = _.Timer(0.3, delayed)
t2.setName('t2')

logging.debug('starting timers')
t1.s..
t2.s..

logging.debug('waiting before canceling @', t2.getName())
t__.s..(0.2)
logging.debug('canceling @', t2.getName())
t2.cancel()
logging.debug('done')