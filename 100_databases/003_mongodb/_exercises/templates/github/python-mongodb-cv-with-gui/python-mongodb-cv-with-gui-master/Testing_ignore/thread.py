_______ threading

# global variable x 
x = 0

___ increment():
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

___ thread_task():
	""" 
	task for thread 
	calls increment function 100000 times. 
	"""
	___ _ __ ra..(100000):
		increment() 

___ main_task():
	global x 
	# setting global variable x as 0 
	x = 0

	# creating threads 
	t1 = threading.Thread(target=thread_task) 
	t2 = threading.Thread(target=thread_task) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

__ __name__ __ "__main__":
	___ i __ ra..(100):
		main_task() 
		print("Iteration {0}: x = {1}".format(i,x)) 
