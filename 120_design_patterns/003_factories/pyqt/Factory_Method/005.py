from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from enum import Enum


class Animal(Enum):
    DOG = 1
    CAT = 2


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animal_types = {
            Animal.DOG: Dog,
            Animal.CAT: Cat
        }
        animal_class = animal_types.get(animal_type)
        return animal_class() if animal_class else None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Factory Method Pattern with Enum Example")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Animal Speak:", self)
        self.label.move(50, 50)

        self.create_button("Dog Speak", Animal.DOG, 50, 100)
        self.create_button("Cat Speak", Animal.CAT, 150, 100)

    def create_button(self, text, animal_type, x, y):
        button = QPushButton(text, self)
        button.move(x, y)
        button.clicked.connect(lambda: self.animal_speak(animal_type))

    def animal_speak(self, animal_type):
        animal = AnimalFactory.create_animal(animal_type)
        if animal:
            self.label.setText(animal.speak())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
