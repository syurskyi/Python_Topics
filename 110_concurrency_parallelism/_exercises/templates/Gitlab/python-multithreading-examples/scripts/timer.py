#!/usr/bin/python


## A Timer starts its work after a delay, 
## and can be canceled at any point within that delay t__ period.


______ _
______ t__
______ logging


logging.basicConfig(
	level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


___ delayed():
    logging.debug('Thread program still running')
    return

___ Main():
	t1 = _.Timer(3, delayed)
	t1.setName('Timer 1')
	t2 = _.Timer(3, delayed)
	t2.setName('Timer 2')

	logging.debug('Starting thread timers')
	t1.s..
	t2.s..

	logging.debug('We are waiting before canceling %s', t2.getName())
	t__.s..(2)
	logging.debug('Now canceling %s', t2.getName())
	t2.cancel()


if __name__ == "__main__":
	Main()