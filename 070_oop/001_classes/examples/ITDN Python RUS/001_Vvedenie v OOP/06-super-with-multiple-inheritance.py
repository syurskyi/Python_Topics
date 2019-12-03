# -*- coding: utf-8 -*-

"""
Пример использования super при множественном наследовании
"""


class Animal(object):
    def __init__(self):
        self.can_fly = False
        self.can_run = False

    def print_abilities(self):
        print(self.__class__.__name__)
        print('Can fly:', self.can_fly)
        print('Can run:', self.can_run)
        print()


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Pegasus(Horse, Bird):
    pass


def main():
    bird = Bird()
    bird.print_abilities()

    horse = Horse()
    horse.print_abilities()

    pegasus = Pegasus()
    pegasus.print_abilities()


if __name__ == '__main__':
    main()