class Singleton(object):

    def __new__(cls):
        # Перекрываем создание объекта класса
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(id(s))
print(s)

b = Singleton()
print(id(b))
print(b)

print(s is b)

# Вывод:
# 140425907838864
# <__main__.Singleton object at 0x7fb7745a9f90>
# 140425907838864
# <__main__.Singleton object at 0x7fb7745a9f90>
# True