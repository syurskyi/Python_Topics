______ l__
______ _
______ t__


___ consumer(cond):
    """wait for the condition and use the resource"""
    l__.d..('Starting consumer thread')
    with cond:
        cond.wait()
        l__.d..('Resource is available to consumer')


___ producer(cond):
    """set up the resource to be used by the consumer"""
    l__.d..('Starting producer thread')
    with cond:
        l__.d..('Making resource available')
        cond.notifyAll()


l__.?(
    ?_l__.D..
    ?_'%(asctime)s (%(threadName)-2s)  _ m.. _,
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