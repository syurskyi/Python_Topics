______ logging
______ _
______ t__


___ consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')


___ producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

condition = _.Condition()
c1 = _.?(name='c1', target=consumer,
                       ?_(condition,))
c2 = _.?(name='c2', target=consumer,
                       ?_(condition,))
p = _.?(name='p', target=producer,
                      ?_(condition,))

c1.s..
t__.s..(0.2)
c2.s..
t__.s..(0.2)
p.s..