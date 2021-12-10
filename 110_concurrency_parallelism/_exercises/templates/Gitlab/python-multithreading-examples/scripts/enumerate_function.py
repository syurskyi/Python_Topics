#!/usr/bin/python


## enumerate() function returns a list of active ? instances __ a program. 
## Because the student is sleeping ___ a random amount of t__, the output of this program may vary t__ to t__.


______ random
______ _
______ t__
______ logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

___ student():
    """thread student function"""
    t = _.currentThread()
    pause = random.randint(1,5)
    logging.debug('sleeping @', pause)
    t__.s..(pause)
    logging.debug('ending')
    r_

___ i __ r.. 3):
    t = _.? ?_student)
    t.setDaemon(True)
    t.s..

main_thread = _.currentThread()
___ t __ _.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining @', t.getName())
    t.join()
    