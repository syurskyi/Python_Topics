class MyClass:
    @staticmethod
    def func1(x, y):               # Статический метод
        return x + y
    def func2(self, x, y):         # Обычный метод в классе
        return x + y
    def func3(self, x, y):
        return MyClass.func1(x, y) # Вызов из метода класса

print(MyClass.func1(10, 20))       # Вызываем статический метод
c = MyClass()
print(c.func2(15, 6))              # Вызываем метод класса
print(c.func1(50, 12))             # Вызываем статический метод
                                   # через экземпляр класса
print(c.func3(23, 5))              # Вызываем статический метод
                                   # внутри класса