# Паттерн Декоратор(decorator) еще один структурный паттерн, который позовляет наделять объекты новыми свойствами и по
# сути является альтернативой наследованию. В отличии от адаптера не меняет интерфейс!

# coding: utf-8

class Man(object):
    """Человек"""

    def __init__(self, name):
        self._name = name

    def say(self):
        print('Привет! Меня зовут %s!' % self._name)


class Jetpack(object):
    """Реактивный ранец"""

    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        # расширяем функциональность объекта добавляя возможность летать
        print('%s летит на реактивном ранце!' % self._man._name)


man = Man('Александр')

man_jetpack = Jetpack(man)
man_jetpack.say()  # Привет! Меня зовут Александр!
man_jetpack.fly()  # Виктор летит на реактивном ранце!