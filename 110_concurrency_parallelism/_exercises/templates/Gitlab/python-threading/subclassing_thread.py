______ _
______ logging


class MyThreadWithArgs(_.?):

    ___ __init__(self, group=N.., target=N.., name=N..,
                  ?_(), kwargs=N.., *, daemon=N..):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    ___ run(self):
        logging.debug('running with @ and @',
                      self.args, self.kwargs)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

___ i __ r.. 5):
    t = MyThreadWithArgs( ?_(i,), kwargs={'a': 'A', 'b': 'B'})
    t.s..