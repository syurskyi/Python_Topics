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
    message = raw_input("Enter a string to store:" )
    background = AsyncWrite(message, 'out.txt')
    #print _.enumerate()
    background.s..
    print "The program can continue while it writes in another thread"
    print "100 + 400 = ", 100+400
    #print _.enumerate()
    background.join()
    print "Waited until thread was complete"
    print _.enumerate()

__ _____ __ ______
    Main()
    
