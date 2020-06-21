import abc

class AbsEmployees(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_employee_info(self, empids):
        pass
