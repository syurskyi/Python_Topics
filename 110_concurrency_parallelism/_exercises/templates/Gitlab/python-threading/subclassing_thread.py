______ _
______ logging


c_ MyThreadWithArgs(_.?):

    ___ - (self, group=N.., target=N.., name=N..,
                  ?_(), kwargs=N.., *, daemon=N..):
        super().- (group=group, target=target, name=name,
                         daemon=daemon)
        args = args
        kwargs = kwargs

    ___ run
        logging.debug('running with @ and @',
                      args, kwargs)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

___ i __ r.. 5):
    t = MyThreadWithArgs( ?_(i,), kwargs={'a': 'A', 'b': 'B'})
    t.s..