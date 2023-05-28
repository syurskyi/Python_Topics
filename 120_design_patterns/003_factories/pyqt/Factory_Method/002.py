from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class Window(QMainWindow):
    def __init__(self, factory):
        super().__init__()
        self.factory = factory
        self.setWindowTitle('Factory Design Pattern Example')
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.label = QLabel('Select an object to create:')
        self.layout.addWidget(self.label)
        self.button1 = QPushButton('Create Object 1')
        self.button1.clicked.connect(self.create_object1)
        self.layout.addWidget(self.button1)
        self.button2 = QPushButton('Create Object 2')
        self.button2.clicked.connect(self.create_object2)
        self.layout.addWidget(self.button2)
        self.setCentralWidget(self.widget)

    def create_object1(self):
        obj = self.factory.create_object1()
        self.label.setText(f'Object created: {obj.name()}')

    def create_object2(self):
        obj = self.factory.create_object2()
        self.label.setText(f'Object created: {obj.name()}')


class Object:
    def name(self):
        pass


class Object1(Object):
    def name(self):
        return 'Object 1'


class Object2(Object):
    def name(self):
        return 'Object 2'


class ObjectFactory:
    def create_object1(self):
        return Object1()

    def create_object2(self):
        return Object2()


if __name__ == '__main__':
    app = QApplication([])
    factory = ObjectFactory()
    window = Window(factory)
    window.show()
    app.exec_()