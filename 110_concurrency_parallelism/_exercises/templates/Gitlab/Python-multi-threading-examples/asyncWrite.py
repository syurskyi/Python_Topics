______ _
______ t__

c_ AsyncWrite(_.?):
	___ - (self, text, out):
		_.?.- (self)
		text = text
		out = out

	___ run
		f = open(out, "a")
		f.write(text + '\n')
		f.close()
		t__.s..(2)
		print "Finished Background file write to " + out

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

