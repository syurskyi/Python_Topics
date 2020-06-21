from abc import ABCMeta, abstractmethod
class MyClass(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def static_func(self, x):     # Абстрактный статический метод
        pass

    @classmethod
    @abstractmethod
    def class_func(self, x):      # Абстрактный метод класса
        pass