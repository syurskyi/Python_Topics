______ _
______ t__

class AsyncWrite(_.?):
	___ __init__(self, text, out):
		_.?.__init__(self)
		self.text = text
		self.out = out

	___ run(self):
		f = open(self.out, "a")
		f.write(self.text + '\n')
		f.close()
		t__.s..(2)
		print "Finished Background file write to " + self.out

___ Main():
	message = raw_input("Enter a string to store:")
	#aa = _.enumerate()
	#print aa
	background = AsyncWrite(message, 'out.txt')
	background.s..
	print "The program ... it writes in another thread"
	print "Waited"
	#aa = _.enumerate()
	#print aa
    	#background.run()
		#print "Waited"
		    #print "Hi"
    	#background.join()
    	#print "Waited until thread was complete"

__ _____ __ ______
		Main()

