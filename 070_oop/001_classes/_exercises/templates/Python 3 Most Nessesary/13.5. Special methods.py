class MyClass:
    def __init__(self, m):
        self.msg = m
    def __call__(self):
        print(self.msg)
c1 = MyClass("Значение1") # Создание экземпляра класса
c2 = MyClass("Значение2") # Создание экземпляра класса
c1()                      # Выведет: Значение1
c2()                      # Выведет: Значение2


class MyClass:
    def __init__(self):
        self.i = 20
    def __getattr__(self, attr):
        print("Вызван метод __getattr__()")
        return 0
c = MyClass()
# Атрибут i существует
print(c.i)     # Выведет: 20. Метод __getattr__() не вызывается
# Атрибут s не существует
print(c.s)     # Выведет: Вызван метод __getattr__() 0


class MyClass:
    def __init__(self):
        self.i = 20
    def __getattribute__(self, attr):
        print("Вызван метод __getattribute__()")
        return object.__getattribute__(self, attr) # Только так!!!
c = MyClass()
print(c.i)     # Выведет: Вызван метод __getattribute__() 20


class MyClass:
    def __setattr__(self, attr, value):
        print("Вызван метод __setattr__()")
        self.__dict__[attr] = value                # Только так!!!
c = MyClass()
c.i = 10       # Выведет: Вызван метод __setattr__()
print(c.i)     # Выведет: 10


class MyClass:
    def __len__(self):
        return 50
c = MyClass()
print(len(c))             # Выведет: 50


class MyClass:
    def __init__(self, m):
        self.msg = m
    def __repr__(self):
        return "Вызван метод __repr__() {0}".format(self.msg)
    def __str__(self):
        return "Вызван метод __str__() {0}".format(self.msg)
c = MyClass("Значение")
print(repr(c)) # Выведет: Вызван метод __repr__() Значение
print(str(c))  # Выведет: Вызван метод __str__() Значение
print(c)       # Выведет: Вызван метод __str__() Значение


class MyClass:
    def __init__(self, y):
        self.x = y
    def __hash__(self):
        return hash(self.x)
c = MyClass(10)
d = {}
d[c] = "Значение"
print(d[c]) # Выведет: Значение