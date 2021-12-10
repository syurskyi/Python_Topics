______ _, t__, random
try:
	______ Queue
except:
	______ queue as Queue

class Producer:
	___ __init__(self):
		self.food = ["ham","soup", "salad"]
		self.nextTime = 0
	___ run(self):
		global q # somewhere else __ the program q is going to be defined
		w___ (t__.clock() < 20):
			if(self.nextTime < t__.clock()):
				f=self.food[random.randrange(len(self.food))]
				q.put(f)
				print "Adding " + f
				self.nextTime += random.random()

class Consumer:
	___ __init__(self):
		self.nextTime = 0;
	___ run(self):
		global q
		w___ (t__.clock() < 20):
			if(self.nextTime<t__.clock() and not q.empty()):
				f=q.get()
				print "Removing " + f
				self.nextTime += random.random()*2

__ _____ __ ______
	q = Queue.Queue(20)

	p = Producer()
	c = Consumer()
	pt = _.? ?_p.run,  ?_())
	
	ct = _.? ?_c.run,  ?_())

	pt.s..
	print  _.enumerate()
	ct.s..
	print  _.enumerate()
	
	print "This is Main"
	print  _.enumerate()
	pt.join()
	print "producer has joined"
	print  _.enumerate()
	ct.join()
	print "consumer has joined"
	print  _.enumerate()
	print "Exiting from Main"
	



