""" 

How this code works?

simply we are incrementing each variable at different period.

variable "a" is incremented at every 1 second
variable "b" is incremented at every 5 seconds
variable "c" is incremented at every 10 seconds

"""


from time import sleep
import threading

a = 0
b = 0
c = 0

class calcA(threading.Thread):
    def __init__(self,name):
        super(calcA, self).__init__()
        self.name = name
        self.terminated = False
        self.start()

    def run(self):
        global a
        print ('starting '+self.name+' thread')
        sleep(1)
        while not self.terminated:
            a += 1
            sleep(1)
            if self.terminated:
                break
        print ('thread '+self.name+' stopped')


class calcB(threading.Thread):
    def __init__(self,name):
        super(calcB, self).__init__()
        self.name = name
        self.terminated = False
        self.start()

    def run(self):
        global b
        print ('starting '+self.name+' thread')
        sleep(1)
        while not self.terminated:
            b += 1
            sleep(5)
            if self.terminated:
                break
        print ('thread '+self.name+' stopped')



class calcC(threading.Thread):
    def __init__(self,name):
        super(calcC, self).__init__()
        self.name = name
        self.terminated = False
        self.start()

    def run(self):
        global c
        print ('starting '+self.name+' thread')
        sleep(1)
        while not self.terminated:
            c += 1
            sleep(10)
            if self.terminated:
                break
        print ('thread '+self.name+' stopped')
# Startup sequence
calcA = calcA(name='incrementA')
sleep(0.1)
calcB = calcB(name='incrementB')
sleep(0.1)
calcC = calcC(name='incrementC')
sleep(0.1)

if __name__ == "__main__":
    try:
    	print 'Press CTRL+C to quit'
    	running = True
        print("a:{} b:{} c:{}".format(a,b,c))

    	while running:
                print("a:{} b:{} c:{}".format(a,b,c))
                sleep(0.1)

    except KeyboardInterrupt:
        print '\nKeyboard Interrupt Detected! Shutting down program!'

        calcA.terminated = True
        calcA.join()
        calcB.terminated = True
        calcB.join()
        calcC.terminated = True
        calcC.join()


    print'\nProcess ended!'
