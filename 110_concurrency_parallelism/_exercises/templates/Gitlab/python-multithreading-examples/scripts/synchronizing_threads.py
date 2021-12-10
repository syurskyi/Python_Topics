______ l__
______ _
______ t__

l__.?(?_l__.D..
                    ?_'%(asctime)s (%(threadName)-2s)  _ m.. _,
                    )

___ consumer(cond):
    """wait for the condition and use the resource"""
    l__.d..('Starting consumer thread')
    t = _.c..
    with cond:
        cond.wait()
        l__.d..('Resource is available to consumer')

___ producer(cond):
    """set up the resource to be used by the consumer"""
    l__.d..('Starting producer thread')
    with cond:
        l__.d..('Making resource available')
        cond.notifyAll()

condition = _.Condition()
c1 = _.?(?_'c1', ?_consumer,  ?_(condition,))
c2 = _.?(?_'c2', ?_consumer,  ?_(condition,))
p = _.?(?_'p', ?_producer,  ?_(condition,))

c1.s..
t__.s..(2)
c2.s..
t__.s..(2)
p.s..
