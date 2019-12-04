class MyClass:
    __slots__ = ["x", "y"]
    def __init__(self, a, b):
        self.x, self.y = a, b
c = MyClass(1, 2)
print(c.x, c.y)                 # Выведет: 1 2
c.x, c.y = 10, 20               # Изменяем значения атрибутов
print(c.x, c.y)                 # Выведет: 10 20
try:                            # Перехватываем исключения
    c.z = 50                    # Атрибут z не указан в __slots__,
                                # поэтому возбуждается исключение
except AttributeError as msg:
    print(msg)                  # 'MyClass' object has no attribute 'z'