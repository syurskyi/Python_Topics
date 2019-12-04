class Class1 (Mixin):
    def method1(self):
        print("Метод класса Class1")

class Class2 (Class1, Mixin):
    def method2(self):
        print("Метод класса Class2")

c1 = Class1()
c1.method1()
c1.mixin_method()                   # Class1 поддерживает метод примеси

c2 = Class2()
c2.method1()
c2.method2()
c2.mixin_method()                   # Class2 также поддерживает метод примеси