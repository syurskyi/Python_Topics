______ logging
______ _
______ t__

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
___ wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

___ wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    w___ not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


e = _.Event()
t1 = _.?(name='block', 
                      target=wait_for_event,
                       ?_(e,))
t1.s..

t2 = _.?(name='non-block', 
                      target=wait_for_event_timeout, 
                       ?_(e, 2))
t2.s..

logging.debug('Waiting before calling Event.set()')
t__.s..(3)
e.set()
logging.debug('Event is set')
