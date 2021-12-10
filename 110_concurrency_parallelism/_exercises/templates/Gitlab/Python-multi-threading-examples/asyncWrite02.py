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
    message = raw_input("Enter a string to store:" )
    background = AsyncWrite(message, 'out.txt')
    #print _.enumerate()
    background.s..
    print "The program can continue while it writes in another thread"
    print "100 + 400 = ", 100+400
    #print _.enumerate()
    background.j..
    print "Waited until thread was complete"
    print _.e..

__ _____ __ ______
    Main()
    
