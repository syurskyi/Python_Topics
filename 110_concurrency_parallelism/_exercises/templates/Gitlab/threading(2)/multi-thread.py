""" 

How this code works?

simply we are incrementing each variable at different period.

variable "a" is incremented at every 1 second
variable "b" is incremented at every 5 seconds
variable "c" is incremented at every 10 seconds

"""


from t__ ______ s..
______ _

a = 0
b = 0
c = 0

c_ calcA(_.?):
    ___ - name):
        super(calcA, self).- ()
        name = name
        terminated = False
        s..

    ___ run
        g.. a
        print ('starting '+name+' thread')
        s..(1)
        w___ n.. terminated:
            a += 1
            s..(1)
            __ terminated:
                break
        print ('thread '+name+' stopped')


c_ calcB(_.?):
    ___ - name):
        super(calcB, self).- ()
        name = name
        terminated = False
        s..

    ___ run
        g.. b
        print ('starting '+name+' thread')
        s..(1)
        w___ n.. terminated:
            b += 1
            s..(5)
            __ terminated:
                break
        print ('thread '+name+' stopped')



c_ calcC(_.?):
    ___ - name):
        super(calcC, self).- ()
        name = name
        terminated = False
        s..

    ___ run
        g.. c
        print ('starting '+name+' thread')
        s..(1)
        w___ n.. terminated:
            c += 1
            s..(10)
            __ terminated:
                break
        print ('thread '+name+' stopped')
# Startup sequence
calcA = calcA(name='incrementA')
s..(0.1)
calcB = calcB(name='incrementB')
s..(0.1)
calcC = calcC(name='incrementC')
s..(0.1)

__ __name__ == "__main__":
    ___
    	print 'Press CTRL+C to quit'
    	running = True
        print("a:{} b:{} c:{}".format(a,b,c))

    	w___ running:
                print("a:{} b:{} c:{}".format(a,b,c))
                s..(0.1)

    except KeyboardInterrupt:
        print '\nKeyboard Interrupt Detected! Shutting down program!'

        calcA.terminated = True
        calcA.j..
        calcB.terminated = True
        calcB.j..
        calcC.terminated = True
        calcC.j..


    print'\nProcess ended!'
