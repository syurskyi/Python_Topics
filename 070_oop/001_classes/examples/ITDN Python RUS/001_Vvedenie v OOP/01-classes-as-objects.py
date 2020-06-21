# -*- coding: utf-8 -*-

# В Python всё является объектами, в том числе
# и сами классы


# Объявление пустого класса MyClass
class MyClass:
    pass

# Создание экземпляра класса
obj = MyClass()

# Объект obj -- это экземпляр класса MyClass,
# то есть он имеет тип MyClass
print(type(obj))  # <class '__main__.MyClass'>

# MyClass -- это класс, но также он является
# и объектом, экземпляром метакласса type,
# являющегося абстракцией понятия типа данных
print(type(MyClass))  # <class 'type'>

# Соответственно, с классами работать как
# с объектами, например, копировать
AnotherClass = MyClass
print(type(AnotherClass))

# Как видим, теперь AnotherClass -- это то же самое, что и MyClass,
# и obj является и экземпляром класса AnotherClass
print(isinstance(obj, AnotherClass))  # True