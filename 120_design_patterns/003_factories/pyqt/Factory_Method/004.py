from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def get_animal_classes():
        return {
            "Dog": Dog,
            "Cat": Cat
        }

    @staticmethod
    def create_animal(animal_type):
        animal_classes = AnimalFactory.get_animal_classes()
        animal_class = animal_classes.get(animal_type, None)
        return animal_class()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animal Factory")
        self.layout = QVBoxLayout(self)
        self.animal_name = QLabel("Enter an animal name:")
        self.animal_name_edit = QLineEdit()
        self.layout.addWidget(self.animal_name)
        self.layout.addWidget(self.animal_name_edit)
        self.create_buttons()
        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

    def create_buttons(self):
        button_layout = QHBoxLayout()
        self.layout.addLayout(button_layout)

        create_dog_btn = QPushButton("Create Dog")
        create_dog_btn.clicked.connect(lambda: self.create_animal("Dog"))
        button_layout.addWidget(create_dog_btn)

        create_cat_btn = QPushButton("Create Cat")
        create_cat_btn.clicked.connect(lambda: self.create_animal("Cat"))
        button_layout.addWidget(create_cat_btn)

    def create_animal(self, animal_type):
        animal = AnimalFactory.create_animal(animal_type)
        if animal:
            self.result_label.setText(animal.speak())



if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
