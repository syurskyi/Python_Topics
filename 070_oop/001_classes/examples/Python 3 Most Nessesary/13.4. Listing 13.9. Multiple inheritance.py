class Class1:         # Базовый класс для класса Class2
    def func1(self):
        print("Метод func1() класса Class1")

class Class2(Class1): # Класс Class2 наследует класс Class1
    def func2(self):
        print("Метод func2() класса Class2")

class Class3(Class1): # Класс Class3 наследует класс Class1
    def func1(self):
        print("Метод func1() класса Class3")
    def func2(self):
        print("Метод func2() класса Class3")
    def func3(self):
        print("Метод func3() класса Class3")
    def func4(self):
        print("Метод func4() класса Class3")

class Class4(Class2, Class3): # Множественное наследование
    def func4(self):
        print("Метод func4() класса Class4")
c = Class4()             # Создаем экземпляр класса Class4
c.func1()                # Выведет: Метод func1() класса Class3
c.func2()                # Выведет: Метод func2() класса Class2
c.func3()                # Выведет: Метод func3() класса Class3
c.func4()                # Выведет: Метод func4() класса Class4