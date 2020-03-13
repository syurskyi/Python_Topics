# -*- coding : utf-8 -*-
#

# abc.ABC basically just an extra layer over metaclass=abc.ABCMeta. i.e abc.ABC implicitly defines the metaclass for us.
# The only difference is that in the former case you need a simple inheritance and in the latter you need
# to specify the metaclass.
# New class ABC has ABCMeta as its meta class. Using ABC as a base class has essentially the same effect as specifying
# metaclass=abc.ABCMeta, but is simpler to type and easier to read.

#
# class abc.ABC
#    A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by
#    simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:
#    from abc import ABC
#
#   class MyABC(ABC):
#        pass
#    Note that the type of ABC is still ABCMeta, therefore inheriting from ABC requires the usual precautions
#    regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define
#    an abstract base class by passing the metaclass keyword and using ABCMeta directly, for example:
#
#    from abc import ABCMeta
#
#   class MyABC(metaclass=ABCMeta):
#       pass
#
#    New in version 3.4.
#
#class abc.ABCMeta
#
#    Metaclass for defining Abstract Base Classes (ABCs).
#    Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class.
#    You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs
#    as “virtual subclasses” – these and their descendants will be considered subclasses of the registering ABC
#    by the built-in issubclass() function, but the registering ABC won’t show up in their
#    MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable
#    (not even via super()). 1

from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    """
    Интерфейс Строителя объявляет создающие методы для различных частей объектов
    Продуктов.
    """

    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass


    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
    конкретные реализации шагов построения. Ваша программа может иметь несколько
    вариантов Строителей, реализованных по-разному.
    """

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой объект продукта,
        который используется в дальнейшей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Конкретные Строители должны предоставить свои собственные методы
        получения результатов. Это связано с тем, что различные типы строителей
        могут создавать совершенно разные продукты с разными интерфейсами.
        Поэтому такие методы не могут быть объявлены в базовом интерфейсе
        Строителя (по крайней мере, в статически типизированном языке
        программирования).

        Как правило, после возвращения конечного результата клиенту, экземпляр
        строителя должен быть готов к началу производства следующего продукта.
        Поэтому обычной практикой является вызов метода сброса в конце тела
        метода getProduct. Однако такое поведение не является обязательным, вы
        можете заставить своих строителей ждать явного запроса на сброс из кода
        клиента, прежде чем избавиться от предыдущего результата.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1:
    """
    Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
    достаточно сложны и требуют обширной конфигурации.

    В отличие от других порождающих паттернов, различные конкретные строители
    могут производить несвязанные продукты. Другими словами, результаты
    различных строителей могут не всегда следовать одному и тому же интерфейсу.
    """

    def __init__(self) -> None:
        self.parts = []      # list

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    Директор отвечает только за выполнение шагов построения в определённой
    последовательности. Это полезно при производстве продуктов в определённом
    порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
    так как клиент может напрямую управлять строителями.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        Директор работает с любым экземпляром строителя, который передаётся ему
        клиентским кодом. Таким образом, клиентский код может изменить конечный
        тип вновь собираемого продукта.
        """
        self._builder = builder

    """
    Директор может строить несколько вариаций продукта, используя одинаковые
    шаги построения.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    Клиентский код создаёт объект-строитель, передаёт его директору, а затем
    инициирует процесс построения. Конечный результат извлекается из объекта-
    строителя.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    d__.b_f_f_p..
    b___.p__.l_p..

    print("\n")

    # Помните, что паттерн Строитель можно использовать без класса Директор.
    print("Custom product: ")
    b___.p_a
    b___.p_b
    b___.p__.l_p..
