from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import QFont

class Animal:
    def __init__(self):
        self.name = None

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self):
        self.name = "Dog"

    def speak(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self):
        self.name = "Cat"

    def speak(self):
        return "Meow!"


class AnimalFactory:
    animal_classes = {
        "Dog": Dog,
        "Cat": Cat
    }

    def create_animal(self, animal_type):
        try:
            animal_class = self.animal_classes[animal_type]
            return animal_class()
        except KeyError:
            return None


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.animal_factory = AnimalFactory()

        self.animal_label = QLabel("Animal Type")
        self.animal_label.setFont(QFont("Arial", 14))

        self.animal_combo_box = QComboBox()
        self.animal_combo_box.setFont(QFont("Arial", 14))
        self.animal_combo_box.addItem("Dog")
        self.animal_combo_box.addItem("Cat")

        self.speak_button = QPushButton("Speak")
        self.speak_button.setFont(QFont("Arial", 14))

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 14))

        self.init_ui()

    def init_ui(self):
        animal_layout = QHBoxLayout()
        animal_layout.addWidget(self.animal_label)
        animal_layout.addWidget(self.animal_combo_box)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.speak_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(animal_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        self.speak_button.clicked.connect(self.speak)

    def speak(self):
        animal_type = self.animal_combo_box.currentText()

        animal = self.animal_factory.create_animal(animal_type)

        if animal is not None:
            self.result_label.setText(animal.speak())
        else:
            self.result_label.setText("Unknown animal type")

if __name__ == '__main__':
    app = QApplication([])
    gui = GUI()
    gui.show()
    app.exec_()
