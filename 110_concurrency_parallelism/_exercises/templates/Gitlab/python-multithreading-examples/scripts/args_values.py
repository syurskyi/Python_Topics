#!/usr/bin/python


## This is not very trivial to access the values of 
## args and kwargs from a subclass as their values are
## being saved __ private variables. 


______ _
______ logging
______ t__


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                   )


class ThreadWithArgs(_.?):
    ___ __init__(self, 
                group=N.., 
                target=N.., 
                name=N..,
                 ?_(),
                kwargs=N.., 
                verbose=N..
                ):

        _.?.__init__(self, 
                                group=group, 
                                target=target, 
                                name=name,
                                verbose=verbose
                                )
        
        self.args = args
        self.kwargs = kwargs
        r_

    ___ run(self):
        logging.debug('This thread is running with @ and @', self.args, self.kwargs)
        r_


___ Main():
    ___ x __ r.. 5):
        myThread = ThreadWithArgs(
             ?_(x,),
            kwargs={'Country':'USA', 'Zip':'12345'}
        )
        myThread.s..
        t__.s..(1)


if __name__ == "__main__":
    Main()
