from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sineWindow_UIs as ui
from math import sin

class sineWidgetClass(QWidget):
    def __init__(self):
        super(sineWidgetClass, self).__init__()
        self.setWindowTitle('Sine')
        self.resize(400, 200)

        self.wave_height = 30
        self.wave_len = 20
        self.penWidth = 3
        self.grid = 30


    def paintEvent(self, event):
        rec = event.rect()
        painter = QPainter()
        painter.begin(self)

        # paint
        painter.fillRect(rec, Qt.black)
        painter.setPen(QPen(QBrush(Qt.gray), 0.5))
        painter.setFont(QFont('Arial', 8))

        for i in range(0, rec.width(), self.grid):
            painter.drawLine(i, 0, i, rec.height())
            if self.grid > 20:
                painter.drawText(i+3, 12, str(i))

        for i in range(0, rec.height(), self.grid):
            painter.drawLine(0, i, rec.width(), i)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen(QBrush(Qt.white), self.penWidth))
        prevx = 0
        prevy = (0*self.wave_height)+(rec.height()/2)
        for x in range(1, rec.width()):
            s = sin((x*0.1)*self.wave_len*0.1)
            # painter.drawPoint(x, (s * self.wave_height) + (rec.height()/2))
            y = (s*self.wave_height)+(rec.height()/2)
            painter.drawLine(QPointF(prevx, prevy), QPointF(x, y))
            prevx = x
            prevy = y
            # print x, y

        # end
        painter.end()

    def setHeight(self, v):
        self.wave_height = v
        self.update()

    def setLen(self, v):
        self.wave_len = v
        self.update()

    def setWidth(self, v):
        self.penWidth = v
        self.update()

    def setGrid(self, v):
        self.grid = v
        self.update()


class sineWindowClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(sineWindowClass, self).__init__()
        self.setupUi(self)
        self.sine = sineWidgetClass()
        self.sine_verticalLayout.addWidget(self.sine)
        self.height_horizontalSlider.setValue(20)
        self.length_horizontalSlider.setValue(20)
        self.grid_horizontalSlider.setValue(30)

        self.height_horizontalSlider.valueChanged.connect(self.sine.setHeight)
        self.length_horizontalSlider.valueChanged.connect(self.sine.setLen)
        self.width_horizontalSlider.valueChanged.connect(self.sine.setWidth)
        self.grid_horizontalSlider.valueChanged.connect(self.sine.setGrid)


if __name__ == '__main__':
    app = QApplication([])
    w = sineWindowClass()
    w.show()
    app.exec_()
