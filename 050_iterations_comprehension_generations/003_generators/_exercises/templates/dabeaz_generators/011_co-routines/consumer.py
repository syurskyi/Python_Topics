# consumer.py
#
# consumer decorator and co-routine example

___ consumer(func):
    ___ start(*args,**kwargs):
        c = func(*args,**kwargs)
        c.send(N..)
        r_ c
    r_ start

# Example
__ __name__ __ '__main__':

    @consumer
    ___ recv_count():
        try:
            while True:
                n = y...
                print("T-minus", n)
        except GeneratorExit:
            print("Kaboom!")

    r = recv_count()
    ___ i __ ra__(5,0,-1):
        r.send(i)

    r.close()

