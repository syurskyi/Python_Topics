# consumer.py
#
# consumer decorator and co-routine example

def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        c.send(N..)
        return c
    return start

# Example
__ __name__ == '__main__':

    @consumer
    def recv_count():
        try:
            while True:
                n = yield
                print("T-minus", n)
        except GeneratorExit:
            print("Kaboom!")

    r = recv_count()
    ___ i __ ra__(5,0,-1):
        r.send(i)

    r.close()

