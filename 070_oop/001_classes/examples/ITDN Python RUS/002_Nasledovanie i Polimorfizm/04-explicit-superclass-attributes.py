# -*- coding: utf-8 -*-

"""
Если в данном классе атрибут или метод был переопределён,
то доступ к соответствующему атрибуту суперкласса можно
получить двумя способами.

Первым из них, который был единственным до появления
Python 2.3 и работает как для классов старого типа, так
и для классов нового типа, является явное обращение к
атрибутам суперкласса по его имени.

Недостатки такого подхода:
 - усложняется рефакторинг и поддержка кода (хотя эта проблема
   решается путём использования таких IDE, как PyCharm);
 - логика кода жёстко привязана к иерархии наследования классов
   и подвержена ошибкам, особенно при использовании множественного
   наследования.
"""


class Base:
    attr = 'Base attribute'

    def method(self):
        print('Base method, current class is', self.__class__.__name__)


class Child(Base):
    attr = 'Redefined attribute'

    @staticmethod
    def get_superclass_attr():
        return Base.attr  # получение атрибута класса Base

    def method(self):  # переопределение метода
        Base.method(self)  # вызов метода суперкласса
        print('Child method, current class is', self.__class__.__name__)


def main():
    print('Base:')
    print(Base.attr)
    base_instance = Base()
    base_instance.method()

    print()

    print('Child:')
    print(Child.attr)
    print(Child.get_superclass_attr())
    child_instance = Child()
    child_instance.method()


if __name__ == '__main__':
    main()
