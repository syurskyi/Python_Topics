______ logging
______ _
______ t__


___ wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: @',event_is_set)



___ wait_for_event_timeout(e,t):

    w___ not e.is_set():

        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: @',event_is_set)

        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


e = _.Event()

t1 = _.?(name='block',target=wait_for_event, ?_(e,))

t1.s..


t2=_.?(name='nonblock',target=wait_for_event_timeout, ?_(e,2))

t2.s..

logging.debug('Waiting before calling Event.set()')
t__.s..(0.3)
e.set()
logging.debug('Event is set')