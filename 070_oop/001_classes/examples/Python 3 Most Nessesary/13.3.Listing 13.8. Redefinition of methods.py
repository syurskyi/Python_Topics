class Class1:                 # Базовый класс
    def __init__(self):
        print("Конструктор базового класса")
    def func1(self):
        print("Метод func1() класса Class1")

class Class2(Class1):         # Класс Class2 наследует класс Class1
    def __init__(self):
        print("Конструктор производного класса")
        Class1.__init__(self) # Вызываем конструктор базового класса
    def func1(self):
        print("Метод func1() класса Class2")
        Class1.func1(self)    # Вызываем метод базового класса

c = Class2()                  # Создаем экземпляр класса Class2
c.func1()                     # Вызываем метод func1()


Class1.__init__(self)          # Вызываем конструктор базового класса


super().__init__()             # Вызываем конструктор базового класса


super(Class2, self).__init__() # Вызываем конструктор базового класса