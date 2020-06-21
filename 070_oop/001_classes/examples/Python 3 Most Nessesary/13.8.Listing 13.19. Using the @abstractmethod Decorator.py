from abc import ABCMeta, abstractmethod
class Class1(metaclass=ABCMeta):
    @abstractmethod
    def func(self, x):     # Абстрактный метод
        pass

class Class2(Class1):      # Наследуем абстрактный метод
    def func(self, x):     # Переопределяем метод
        print(x)
class Class3(Class1):      # Класс не переопределяет метод
    pass

c2 = Class2()
c2.func(50)                # Выведет: 50
try:
    c3 = Class3()          # Ошибка. Метод func() не переопределен
    c3.func(50)
except TypeError as msg:
    print(msg)             # Can't instantiate abstract class Class3
                           # with abstract methods func