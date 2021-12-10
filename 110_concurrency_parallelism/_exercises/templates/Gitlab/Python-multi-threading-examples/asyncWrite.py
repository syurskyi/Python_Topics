import threading
import time

class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out

	def run(self):
		f = open(self.out, "a")
		f.write(self.text + '\n')
		f.close()
		time.sleep(2)
		print "Finished Background file write to " + self.out

def Main():
	message = raw_input("Enter a string to store:")
	#aa = threading.enumerate()
	#print aa
	background = AsyncWrite(message, 'out.txt')
	background.start()
	print "The program ... it writes in another thread"
	print "Waited"
	#aa = threading.enumerate()
	#print aa
    	#background.run()
		#print "Waited"
		    #print "Hi"
    	#background.join()
    	#print "Waited until thread was complete"

if __name__ == '__main__':
		Main()

