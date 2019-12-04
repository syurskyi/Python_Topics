class Class1:
    def func(self, x):     # Абстрактный метод
        # Возбуждаем исключение с помощью raise
        raise NotImplementedError("Необходимо переопределить метод")

class Class2(Class1):      # Наследуем абстрактный метод
    def func(self, x):     # Переопределяем метод
        print(x)

class Class3(Class1):      # Класс не переопределяет метод
    pass

c2 = Class2()
c2.func(50)                # Выведет: 50
c3 = Class3()
try:                       # Перехватываем исключения
    c3.func(50)            # Ошибка. Метод func() не переопределен
except NotImplementedError as msg:
    print(msg)             # Выведет: Необходимо переопределить метод