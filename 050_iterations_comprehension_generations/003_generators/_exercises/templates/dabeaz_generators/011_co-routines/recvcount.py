# recvcount.py
#
# Example of a co-routine

___ recv_count():
    try:
        while True:
            n = (y...)
            print("T-minus", n)
    except GeneratorExit:
        print("Kaboom!")

r = recv_count()
r.send(N..)
___ i __ ra__(5,0,-1):
    r.send(i)

r.close()

