______ l__
______ _
______ t__


___ wait_for_event(e):
    l__.d..('wait_for_event starting')
    event_is_set = e.wait()
    l__.d..('event set: @',event_is_set)



___ wait_for_event_timeout(e,t):

    w___ n.. e.is_set():

        l__.d..('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        l__.d..('event set: @',event_is_set)

        __ event_is_set:
            l__.d..('processing event')
        else:
            l__.d..('doing other work')


l__.?(
    ?_l__.D..
    ?_ _threadName)-10s)  _ m.. _,
)


e = _.Event()

t1 = _.?(name='block',target=wait_for_event, ?_(e,))

t1.s..


t2=_.?(name='nonblock',target=wait_for_event_timeout, ?_(e,2))

t2.s..

l__.d..('Waiting before calling Event.set()')
t__.s..(0.3)
e.set()
l__.d..('Event is set')