# -*- coding: utf-8 -*-

# Context Manager Protocol
class MyClass:
    def __enter__(self):
        print("Call method __enter__()")
        return self
    def __exit__(self, Type, Value, Trace):
        print("Call method __exit__()")
        if Type is None:  # Если исключение не возникло
            print("Exception not")
        else:             # Если возникло исключение
            print("Value =", Value)
            return False  # False — исключение не обработано
                          # True  — исключение обработано
print("Последовательность при отсутствии исключения:")
with MyClass():
    print("Блок внутри with")
print("\nПоследовательность при наличии исключения:")
with MyClass() as obj:
    print("Блок внутри with")
    raise TypeError("Исключение TypeError")