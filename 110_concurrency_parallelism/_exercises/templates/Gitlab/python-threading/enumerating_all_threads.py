______ r__
______ _
______ t__
______ logging


___ worker():
    """thread worker function"""
    pause = r__.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    t__.s..(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

___ i __ r.. 3):
    t = _.? ?_worker, daemon=True)
    t.s..

main_thread = _.main_thread()
___ t __ _.e..:
    __ t is main_thread:
        continue
    logging.debug('joining @', t.getName())
    t.j..