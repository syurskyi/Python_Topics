class MyClass:
    def __init__(self, y):
        self.x = y
    def __add__(self, y):            # Перегрузка оператора +
        print("Экземпляр слева")
        return self.x + y
    def __radd__(self, y):           # Перегрузка оператора +
        print("Экземпляр справа")
        return self.x + y
    def __iadd__(self, y):           # Перегрузка оператора +=
        print("Сложение с присваиванием")
        self.x += y
        return self
c = MyClass(50)
print(c + 10)                 # Выведет: Экземпляр слева 60
print(20 + c)                 # Выведет: Экземпляр справа 70
c += 30                       # Выведет: Сложение с присваиванием
print(c.x)                    # Выведет: 80