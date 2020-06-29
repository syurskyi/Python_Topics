from PySide.QtCore ______ *
from PySide.QtGui ______ *

______ math
try:
    ______ ?
except:pass

sliderStyle = '''QSlider::groove:vertical {
    border: 1px solid #ffaa00;
    background: #ffaa00;
    width: 6px;
    border-radius: 2px;
}


QSlider::add-page:vertical {
    background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
        stop: 0 #ffaa00, stop: 1 #ffaa00);
    background:#ffaa00;
    border: 1px solid #777;
    width: 10px;
    border-radius: 2px;
}

QSlider::sub-page:vertical {
    background: rgb(40,40,40);
    border: 1px solid #777;
    width: 10px;
    border-radius: 2px;
}

QSlider::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #eee, stop:1 #ccc);
    border: 1px solid #777;
    height: 7px;
    margin-left: -5px;
    margin-right: -5px;
    border-radius: 2px;
}

QSlider::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #fff, stop:1 #ddd);
    border: 1px solid #444;
    border-radius: 2px;
}

QSlider::add-page:vertical:disabled {
    background: #bbb;
    border-color: #999;
}

QSlider::sub-page:vertical:disabled {
    background: #eee;
    border-color: #999;
}

QSlider::handle:vertical:disabled {
    background: #eee;
    border: 1px solid #aaa;
    border-radius: 2px;
}'''
widgetStyle = '''
        QLineEdit
        {
            background-color: rgb(50,50,50);
            color:#fff;
            padding: 1px;
            border-style: solid;
            border: 1px solid #1e1e1e;
            border-radius: 2;
        }
        QLabel
        {
            color:white;
        }
        QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
            color: #b1b1b1;
            background-color: #323232;
            border: 2px solid #b1b1b1;
            border-radius: 4px;
        }

        QRadioButton::indicator:checked
        {
            background-color: qradialgradient(
                cx: 0.5, cy: 0.5,
                fx: 0.5, fy: 0.5,
                radius: 1.0,
                stop: 0.25 #ffaa00,
                stop: 0.3 #323232
            );
        }

        QRadioButton::indicator
        {
            border-radius: 2px;
        }

        QRadioButton::indicator:hover
        {
            border: 2px solid #ffaa00;
        }
        QRadioButton
        {
            color:#fff;
        }

        '''
c_ colorWheelClass(QWidget):
    colorChangedSignal = Signal(list)
    ___  - (self):
        super(colorWheelClass, self). - ()
        self.hw = 200
        self.padding = 2
        self.blackBorder = 10
        self.radius = (self.hw / 2) - self.padding
        self.center = self.hw / 2
        self.setFixedSize(QSize(self.hw, self.hw))
        self.img = None
        self.pick = [0, 0]
        self.pickerSize = 8
        self.value = 0

    ___ paintEvent(self, event):
        __ not self.img:
            self.img = self.getCircle()
        painter = QPainter()
        painter.begin(self)
        #wheel
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawImage(0, 0, self.img)
        #value
        painter.setPen(Qt.NoPen)
        elipse = QPainterPath()
        elipse.addEllipse(QRect(self.blackBorder, self.blackBorder, self.hw-self.blackBorder*2,self.hw-self.blackBorder*2))
        painter.setBrush(QColor(0,0,0,self.value*255))
        painter.drawPath(elipse)


        #picker
        x = self.center + self.pick[0]
        y = self.center + self.pick[1]
        #line
        painter.setBrush(Qt.NoBrush)
        lineColor = 55 __ self.value < 0.5 ____ 200
        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 1))
        painter.drawLine(self.center, self.center,x, y)

        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 1, Qt.DashLine))
        size = math.sqrt((self.pick[0] * self.pick[0]) + (self.pick[1] * self.pick[1]))
        painter.drawEllipse(self.center-size,
                            self.center-size,
                            size*2,
                            size*2)
        #decorate
        painter.setPen(QPen(QColor(255,255,255), 3))
        c1 = self.padding
        c2 = self.hw - self.padding*2
        painter.drawEllipse(c1,c1,c2,c2)

        #picker circle
        painter.setPen(QPen(QColor(55,55,55), 2))
        painter.setBrush(QBrush(QColor(255,255,255)))
        #painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(x-self.pickerSize*0.5,
                            y-self.pickerSize*0.5,
                            self.pickerSize,
                            self.pickerSize)
        painter.end()

    ___ mousePressEvent(self, event):
        self.setPickerPos(event.pos())
        QWidget.mousePressEvent(self, event)

    ___ mouseMoveEvent(self, event):
        self.setPickerPos(event.pos())
        QWidget.mouseMoveEvent(self, event)

    ___ setPickerPos(self, pos):
        x = pos.x()-self.center
        y = pos.y() - self.center
        distance = math.sqrt((x * x) + (y * y))
        __ distance < self.radius:
            self.pick = [x, y]
            self.update()
        ____
            over = self.radius / distance
            self.pick = [x*over, y*over]
            self.update()
        self.updateColor()

    ___ updateColor(self):
        x = self.pick[0]
        y = self.pick[1]
        distance = math.sqrt((x * x) + (y * y))
        angle = math.degrees(math.atan2(y,x))
        __ angle < 0:
            angle += 360
        s = min(1, distance / self.radius)
        self.colorChangedSignal.emit([angle/360,s])

    ___ sV..(self, v):
        self.value = (1000-v) * 0.001
        self.update()
        self.updateColor()

    ___ getCircle(self):
        img = QImage(self.hw, self.hw, QImage.Format_ARGB32)

        color = QColor()
        ___ y __ ra..(-self.center, self.center):
            ___ x __ ra..(-self.center, self.center):
                distance = math.sqrt((x * x) + (y * y))
                __ distance > self.radius:
                    color.setRgb(0.0, 0.0, 0.0)
                    color.setAlpha(0.0)
                ____
                    s = distance / self.radius
                    angle = (math.atan2(y, x) * 180 / math.pi)
                    __ y < 0:
                        angle += 360
                    h = angle / 360.0
                    v = 1
                    color.setHsvF(h, s, v, 1.0)
                img.setPixel(x+self.center, y+self.center, color.rgba())
        return img


c_ colorRampClass(QWidget):
    colorChangedSignal = Signal(list)
    ___  - (self):
        super(colorRampClass, self). - ()
        self.hw = 200
        self.setFixedSize(QSize(self.hw, self.hw))
        self.padding = 2
        self.value = 0.0
        self.pick = [0, 0]
        self.img = None
        self.pickerSize = 8

    ___ paintEvent(self, event):
        __ not self.img:
            self.img = self.getRamp()
        painter = QPainter()
        painter.begin(self)
        #wheel
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawImage(0, 0, self.img)
        #value
        painter.setPen(Qt.NoPen)
        painter.fillRect(0,0, self.hw, self.hw, QColor(0,0,0,self.value*255))
        #lines
        x = self.pick[0]
        y = self.pick[1]
        lineColor = 55 __ self.value < 0.5 ____ 200
        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 0.5))
        painter.drawLine(x,0,x,self.hw)
        painter.drawLine(0,y,self.hw,y)
        #picker

        painter.setPen(QPen(QColor(55,55,55), 2))
        painter.setBrush(QBrush(QColor(255,255,255)))
        painter.drawEllipse(x-self.pickerSize*0.5,
                            y-self.pickerSize*0.5,
                            self.pickerSize,
                            self.pickerSize)
        painter.end()

    ___ updateColor(self):
        h = self.pick[0]/float(self.hw)
        s = self.pick[1]/float(self.hw)
        self.colorChangedSignal.emit([h,s])

    ___ sV..(self, v):
        self.value = (1000-v) * 0.001
        self.update()
        self.updateColor()

    ___ mousePressEvent(self, event):
        self.setPickerPos(event.pos())
        QWidget.mousePressEvent(self, event)

    ___ mouseMoveEvent(self, event):
        self.setPickerPos(event.pos())
        QWidget.mouseMoveEvent(self, event)

    ___ setPickerPos(self, pos):
        x = pos.x()
        y = pos.y()
        __ x < 0:
            x = 0
        __ x > self.hw:
            x = self.hw
        __ y < 0:
            y = 0
        __ y > self.hw:
            y = self.hw
        self.pick = [x, y]
        self.update()
        self.updateColor()

    ___ getRamp(self):
        img = QImage(self.hw, self.hw, QImage.Format_RGB32)
        color = QColor()
        ___ y __ ra..(self.hw):
            ___ x __ ra..(self.hw):
                h = x / float(self.hw)
                s = y/ float(self.hw)
                color.setHsvF(h, s, 1)
                img.setPixel(x, y, color.rgb())
        return img


c_ colorPickerClass(QWidget):
    ___  - (self, nukeNode=None, knob=None, label='Empty'):
        super(colorPickerClass, self). - ()
        #window
        self.resize(QSize(250, 340))
        self.setStyleSheet(widgetStyle)
        #variables
        self.nukeNode = nukeNode
        self.knob = knob
        self.picker = None
        #ui
        mainLy = QVBoxLayout()
        self.setLayout(mainLy)
        #picker switcher
        lab = QLabel(label)
        mainLy.addWidget(lab)
        switch_ly = QHBoxLayout()
        self.rb1 = QRadioButton()
        self.rb1.setText('Circle')
        self.rb1.setChecked(1)
        self.rb1.clicked.connect(self.addPicker)
        switch_ly.addWidget(self.rb1)
        self.rb2 = QRadioButton()
        self.rb2.clicked.connect(self.addPicker)
        self.rb2.setText('Square')
        switch_ly.addWidget(self.rb2)
        mainLy.addLayout(switch_ly)

        #color swatch
        self.color = QLabel()
        mainLy.addWidget(self.color)
        ly = QHBoxLayout()
        self.picker_ly = QVBoxLayout()
        self.picker_ly.setContentsMargins(0,0,0,0)
        ly.addLayout(self.picker_ly)
        #value
        self.value = QSlider(Qt.Vertical)
        self.value.setStyleSheet(sliderStyle)
        self.value.setMaximumHeight(200)
        ly.addWidget(self.value)
        self.value.setRange(0,1000)
        self.value.sV..(1000)
        mainLy.addLayout(ly)
        #color values
        self.grid_ly = QGridLayout()
        self.hex_lb = QLabel()
        self.hex_lb.setLayoutDirection(Qt.RightToLeft)
        self.hex_lb.setText("HEX")
        self.grid_ly.addWidget(self.hex_lb, 0, 0, 1, 1)
        self.hex_le = QLineEdit()
        self.grid_ly.addWidget(self.hex_le, 0, 1, 1, 1)

        self.rgb_lb = QLabel()
        self.rgb_lb.setLayoutDirection(Qt.RightToLeft)
        self.rgb_lb.setText("RGB")
        self.grid_ly.addWidget(self.rgb_lb, 1, 0, 1, 1)
        self.rgb_le = QLineEdit()
        self.grid_ly.addWidget(self.rgb_le, 1, 1, 1, 1)

        self.hsv_lb = QLabel()
        self.hsv_lb.setLayoutDirection(Qt.RightToLeft)
        self.hsv_lb.setText("HSV")
        self.grid_ly.addWidget(self.hsv_lb, 2, 0, 1, 1)
        self.hsv_le = QLineEdit()
        self.grid_ly.addWidget(self.hsv_le, 2, 1, 1, 1)

        mainLy.addLayout(self.grid_ly)
        mainLy.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        #START

        self.addPicker()
        self.picker.updateColor()

    ___ addPicker(self):
        __ self.picker:
            self.picker.setParent(None)
        __ self.rb1.isChecked():
            self.picker = colorWheelClass()
        ____
            self.picker = colorRampClass()

        self.picker.colorChangedSignal.connect(self.receiveColor)
        self.picker_ly.addWidget(self.picker)
        self.value.valueChanged.connect(self.picker.sV..)
        self.picker.sV..(self.value.value())
        self.picker.updateColor()

    ___ setPickerIcon(self):
        pix = QPixmap(32,32)
        pix.fill(QColor(Qt.red))
        self.setWindowIcon(QIcon(pix))

    ___ receiveColor(self, hs):
        v = self.value.value()*0.001
        c = QColor()
        c.setHsvF(hs[0], hs[1], v)
        self.updateColor(c)

    ___ updateColor(self, color):
        self.color.setStyleSheet('''
        QWidget{
            background-color:%s;
            border-style: solid;
            border: 1px solid #fff;
            border-radius: 2;
        }''' % color.name())
        #hex
        self.hex_le.setText(color.name())
        #rgb
        self.rgb_le.setText('%d,%d,%d' % (color.red(), color.green(), color.blue()))
        #hsv
        self.hsv_le.setText('{0},{1},{2}'.format(*color.getHsv()))
        __ self.nukeNode:
            knob = self.nukeNode.knob(self.knob)
            __ knob:
                knob.sV..([color.red()/255.0, color.green()/255.0, color.blue()/255.0, 1])
            ____
                ?.tprint('%s, %s ' % (self.knob, knob))



___ addTab(node):
    tab = node.findChild(QTabWidget)
    w = QWidget()
    ly = QHBoxLayout()
    w.setLayout(ly)
    cp1 = colorPickerClass(?.toNode(node.objectName()),'shadows.gain', 'Shadows')
    cp2 = colorPickerClass(?.toNode(node.objectName()),'midtones.gain', 'Mid tone')
    cp3 = colorPickerClass(?.toNode(node.objectName()),'highlights.gain', 'Highlights')
    ly.addWidget(cp1)
    ly.addWidget(cp2)
    ly.addWidget(cp3)

    tab.insertTab(0, w, 'Color Wheels')
    tab.setCurrentIndex(0)
    node.resize(777, 670)


__ __name__ == '__main__':
    app = QApplication([])
    s = colorPickerClass()
    s.show()
    app.exec_()