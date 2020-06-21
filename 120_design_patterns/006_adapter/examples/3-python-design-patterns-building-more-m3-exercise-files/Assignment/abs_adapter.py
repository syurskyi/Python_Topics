import abc

class AbsAdapter(metaclass=abc.ABCMeta):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def first_name(self):
        pass

    @abc.abstractproperty
    def last_name(self):
        pass

    @abc.abstractproperty
    def address(self):
        pass

    @abc.abstractproperty
    def number(self):
        pass

    @abc.abstractproperty
    def street(self):
        pass
