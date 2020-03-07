import abc

class AbsFacade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_twitter(self):
        pass
