# -*- coding: utf-8 -*-


"""
Ещё один пример использования super и построения интерпретатором линеаризации.
Иерархия классов в данном примере:
            object
            /    \
           /      \
          A        B
          \       /|
           \     / |
            \   /  |
             \ /   |
              C    |
              \    |
               \   |
                \  |
                 \ |
                  \|
                   D
                   |
                   E
"""



def gen_init(cls):
    """
    Декоратор gen_init, который добавляет автоматически
    сгенерированный конструктор.
    Декоратор -- это функция, которая принимает функцию или класс
    и возвращает другой объект, который будет привязан к имени изначального.
    Обычно используется для изменения поведения фукнции (путём создания
    новой функции, которая вызывает изначальную) или модификации класса
    (и происходит в данном примере).

    :param cls: модифицируемый класс
    :return:    класс с добавленным конструктором
    """

    def init(self):
        print('Entered', cls.__name__, "constructor")
        super(cls, self).__init__()
        print('Quit', cls.__name__, "constructor")
    cls.__init__ = init
    return cls


@gen_init
class A(object):
    pass


@gen_init
class B(object):
    pass


@gen_init
class C(A, B):
    pass


@gen_init
class D(C, B):
    pass


@gen_init
class E(D):
    pass


print(E.__mro__)
obj = E()