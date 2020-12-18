# -*- coding: utf-8

"""
Порядок разрешения методов при ромбовидном множественном наследовании.

Здесь не указано, что класс A наследуется от object.
В Python 3 данный класс будет унаследован от него по умолчанию.
В Python 2 результатом будет создание класса старого типа, для
которого не строится линеаризация. В классах старого типа поиск
атрибутов производится в порядке обхода суперклассов в глубину,
поэтому в Python 2 результатом будет "A method", а в Python3 --
"C method". В предыдущем же примере обе версии интерпретатора
вызовут метод класса C. При этом согласно иерархии классов
именно метод класса C и должен быть вызван. Поэтому (а также
некоторым другим причинам) при использовании Python 2 следует
всегда наследовать создаваемые классы от object либо другого
стандартного типа данных (все они являются классами нового типа).
"""

class A:
    def method(self):
        print('A method')


class B(A):
    pass


class C(A):
    def method(self):
        print('C method')


class D (B, C):
    pass


obj = D()

obj.method()