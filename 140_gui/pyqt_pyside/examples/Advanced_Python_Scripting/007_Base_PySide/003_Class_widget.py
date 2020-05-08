from PySide2.QtWidgets import *


class MyWidget(QWidget):                          # NAdo sozdat' svoj klass ynasledovanuj ot nyznogo nam vidgeta
    def __init__(self):
        super(MyWidget, self).__init__()
        l = QVBoxLayout()                         # i kogda mu sozdajom interface dlja nego
        self.setLayout(l)                         # nyzno obrachatsja k ekzempljary cherz self
        label = QLabel('Text')
        l.addWidget(label)
        b = QPushButton('OK')
        l.addWidget(b)


app = QApplication([])
w = MyWidget()
w.show()
app.exec_()