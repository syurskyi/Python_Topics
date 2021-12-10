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


c_ ThreadWithArgs(_.?):
    ___ - (self, 
                group=N.., 
                target=N.., 
                name=N..,
                 ?_(),
                kwargs=N.., 
                verbose=N..
                ):

        _.?.- (self, 
                                group=group, 
                                target=target, 
                                name=name,
                                verbose=verbose
                                )
        
        args = args
        kwargs = kwargs
        r_

    ___ run
        logging.debug('This thread is running with @ and @', args, kwargs)
        r_


___ Main():
    ___ x __ r.. 5):
        myThread = ThreadWithArgs(
             ?_(x,),
            kwargs={'Country':'USA', 'Zip':'12345'}
        )
        myThread.s..
        t__.s..(1)


__ __name__ == "__main__":
    Main()
