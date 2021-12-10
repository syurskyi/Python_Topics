#!/usr/bin/python


## This program creates a thread, 
## officially names it and 
## tries to print the name


______ _
______ t__


___ ThreadFunction():
	print _.currentThread().getName(), "Starting"
	t__.s..(2)
	print _.currentThread().getName(), "Exiting"

___ ServiceFunction():
	print _.currentThread().getName(), "Starting"
	t__.s..(3)
	print _.currentThread().getName(), "Exiting"


___ Main():
	myThread = _.?(
		name='Service Function', 
		target=ServiceFunction
	)
	w = _.?(
		name='Thread function',
		target=ThreadFunction
	)
	w2 = _.?(
		target=ThreadFunction
	)

	w.s..
	w2.s..
	myThread.s..


if __name__ == "__main__":
	Main()
