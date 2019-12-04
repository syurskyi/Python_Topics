class MyClass:
    @classmethod
    def func(cls, x): # Метод класса
        print(cls, x)
MyClass.func(10)      # Вызываем метод через название класса
c = MyClass()
c.func(50)            # Вызываем метод класса через экземпляр