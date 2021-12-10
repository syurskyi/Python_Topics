import threading, time, random
try:
	import Queue
except:
	import queue as Queue

class Producer:
	def __init__(self):
		self.food = ["ham","soup", "salad"]
		self.nextTime = 0
	def run(self):
		global q # somewhere else in the program q is going to be defined
		while (time.clock() < 20):
			if(self.nextTime < time.clock()):
				f=self.food[random.randrange(len(self.food))]
				q.put(f)
				print "Adding " + f
				self.nextTime += random.random()

class Consumer:
	def __init__(self):
		self.nextTime = 0;
	def run(self):
		global q
		while (time.clock() < 20):
			if(self.nextTime<time.clock() and not q.empty()):
				f=q.get()
				print "Removing " + f
				self.nextTime += random.random()*2

if __name__ == '__main__':
	q = Queue.Queue(20)

	p = Producer()
	c = Consumer()
	pt = threading.Thread(target=p.run, args=())
	
	ct = threading.Thread(target=c.run, args=())

	pt.start()
	print  threading.enumerate()
	ct.start()
	print  threading.enumerate()
	
	print "This is Main"
	print  threading.enumerate()
	pt.join()
	print "producer has joined"
	print  threading.enumerate()
	ct.join()
	print "consumer has joined"
	print  threading.enumerate()
	print "Exiting from Main"
	



