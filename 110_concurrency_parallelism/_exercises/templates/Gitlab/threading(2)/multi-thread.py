""" 

How this code works?

simply we are incrementing each variable at different period.

variable "a" is incremented at every 1 second
variable "b" is incremented at every 5 seconds
variable "c" is incremented at every 10 seconds

"""


____ t__ ______ s..
______ _

a = 0
b = 0
c = 0

c_ calcA(_.?):
    ___ - name):
        s__(calcA, .- ()
        name = name
        terminated = F..
        s..

    ___ run
        g.. a
        print ('starting '+name+' thread')
        s..(1)
        w___ n.. terminated:
            a += 1
            s..(1)
            __ terminated:
                ____
        print ('thread '+name+' stopped')


c_ calcB(_.?):
    ___ - name):
        s__(calcB, .- ()
        name = name
        terminated = F..
        s..

    ___ run
        g.. b
        print ('starting '+name+' thread')
        s..(1)
        w___ n.. terminated:
            b += 1
            s..(5)
            __ terminated:
                ____
        print ('thread '+name+' stopped')



c_ calcC(_.?):
    ___ - name):
        s__(calcC, .- ()
        name = name
        terminated = F..
        s..

    ___ run
        g.. c
        print ('starting '+name+' thread')
        s..(1)
        w___ n.. terminated:
            c += 1
            s..(10)
            __ terminated:
                ____
        print ('thread '+name+' stopped')
# Startup sequence
calcA = calcA(?_'incrementA')
s..(0.1)
calcB = calcB(?_'incrementB')
s..(0.1)
calcC = calcC(?_'incrementC')
s..(0.1)

__ ____ __ ______:
    ___
    	print 'Press CTRL+C to quit'
    	running = T..
        print("a:{} b:{} c:{}".format(a,b,c))

    	w___ running:
                print("a:{} b:{} c:{}".format(a,b,c))
                s..(0.1)

    except KeyboardInterrupt:
        print '\nKeyboard Interrupt Detected! Shutting down program!'

        calcA.terminated = T..
        calcA.j..
        calcB.terminated = T..
        calcB.j..
        calcC.terminated = T..
        calcC.j..


    print'\nProcess ended!'
