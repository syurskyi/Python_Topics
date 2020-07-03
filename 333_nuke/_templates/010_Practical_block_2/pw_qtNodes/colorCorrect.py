____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

______ math
___
    ______ ?
______pass

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
c_ colorWheelClass(?W..):
    colorChangedSignal = Signal(list)
    ___  -
        s_(colorWheelClass, self). - ()
        hw = 200
        padding = 2
        blackBorder = 10
        radius = (hw / 2) - padding
        center = hw / 2
        setFixedSize(QSize(hw, hw))
        img = N..
        pick = [0, 0]
        pickerSize = 8
        value = 0

    ___ paintEvent(self, event):
        __ no. img:
            img = getCircle()
        painter = QPainter()
        painter.begin(self)
        #wheel
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawImage(0, 0, img)
        #value
        painter.setPen(Qt.NoPen)
        elipse = QPainterPath()
        elipse.addEllipse(QRect(blackBorder, blackBorder, hw-blackBorder*2,hw-blackBorder*2))
        painter.setBrush(QColor(0,0,0,value*255))
        painter.drawPath(elipse)


        #picker
        x = center + pick[0]
        y = center + pick[1]
        #line
        painter.setBrush(Qt.NoBrush)
        lineColor = 55 __ value < 0.5 ____ 200
        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 1))
        painter.drawLine(center, center,x, y)

        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 1, Qt.DashLine))
        size = math.sqrt((pick[0] * pick[0]) + (pick[1] * pick[1]))
        painter.drawEllipse(center-size,
                            center-size,
                            size*2,
                            size*2)
        #decorate
        painter.setPen(QPen(QColor(255,255,255), 3))
        c1 = padding
        c2 = hw - padding*2
        painter.drawEllipse(c1,c1,c2,c2)

        #picker circle
        painter.setPen(QPen(QColor(55,55,55), 2))
        painter.setBrush(QBrush(QColor(255,255,255)))
        #painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(x-pickerSize*0.5,
                            y-pickerSize*0.5,
                            pickerSize,
                            pickerSize)
        painter.end()

    ___ mousePressEvent(self, event):
        setPickerPos(event.pos())
        ?W...mousePressEvent(self, event)

    ___ mouseMoveEvent(self, event):
        setPickerPos(event.pos())
        ?W...mouseMoveEvent(self, event)

    ___ setPickerPos(self, pos):
        x = pos.x()-center
        y = pos.y() - center
        distance = math.sqrt((x * x) + (y * y))
        __ distance < radius:
            pick = [x, y]
            update()
        ____
            over = radius / distance
            pick = [x*over, y*over]
            update()
        updateColor()

    ___ updateColor
        x = pick[0]
        y = pick[1]
        distance = math.sqrt((x * x) + (y * y))
        angle = math.degrees(math.atan2(y,x))
        __ angle < 0:
            angle += 360
        s = min(1, distance / radius)
        colorChangedSignal.emit([angle/360,s])

    ___ sV..(self, v):
        value = (1000-v) * 0.001
        update()
        updateColor()

    ___ getCircle
        img = QImage(hw, hw, QImage.Format_ARGB32)

        color = QColor()
        ___ y __ ra..(-center, center):
            ___ x __ ra..(-center, center):
                distance = math.sqrt((x * x) + (y * y))
                __ distance > radius:
                    color.setRgb(0.0, 0.0, 0.0)
                    color.setAlpha(0.0)
                ____
                    s = distance / radius
                    angle = (math.atan2(y, x) * 180 / math.pi)
                    __ y < 0:
                        angle += 360
                    h = angle / 360.0
                    v = 1
                    color.setHsvF(h, s, v, 1.0)
                img.setPixel(x+center, y+center, color.rgba())
        r_ img


c_ colorRampClass(?W..):
    colorChangedSignal = Signal(list)
    ___  -
        s_(colorRampClass, self). - ()
        hw = 200
        setFixedSize(QSize(hw, hw))
        padding = 2
        value = 0.0
        pick = [0, 0]
        img = N..
        pickerSize = 8

    ___ paintEvent(self, event):
        __ no. img:
            img = getRamp()
        painter = QPainter()
        painter.begin(self)
        #wheel
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawImage(0, 0, img)
        #value
        painter.setPen(Qt.NoPen)
        painter.fillRect(0,0, hw, hw, QColor(0,0,0,value*255))
        #lines
        x = pick[0]
        y = pick[1]
        lineColor = 55 __ value < 0.5 ____ 200
        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 0.5))
        painter.drawLine(x,0,x,hw)
        painter.drawLine(0,y,hw,y)
        #picker

        painter.setPen(QPen(QColor(55,55,55), 2))
        painter.setBrush(QBrush(QColor(255,255,255)))
        painter.drawEllipse(x-pickerSize*0.5,
                            y-pickerSize*0.5,
                            pickerSize,
                            pickerSize)
        painter.end()

    ___ updateColor
        h = pick[0]/float(hw)
        s = pick[1]/float(hw)
        colorChangedSignal.emit([h,s])

    ___ sV..(self, v):
        value = (1000-v) * 0.001
        update()
        updateColor()

    ___ mousePressEvent(self, event):
        setPickerPos(event.pos())
        ?W...mousePressEvent(self, event)

    ___ mouseMoveEvent(self, event):
        setPickerPos(event.pos())
        ?W...mouseMoveEvent(self, event)

    ___ setPickerPos(self, pos):
        x = pos.x()
        y = pos.y()
        __ x < 0:
            x = 0
        __ x > hw:
            x = hw
        __ y < 0:
            y = 0
        __ y > hw:
            y = hw
        pick = [x, y]
        update()
        updateColor()

    ___ getRamp
        img = QImage(hw, hw, QImage.Format_RGB32)
        color = QColor()
        ___ y __ ra..(hw):
            ___ x __ ra..(hw):
                h = x / float(hw)
                s = y/ float(hw)
                color.setHsvF(h, s, 1)
                img.setPixel(x, y, color.rgb())
        r_ img


c_ colorPickerClass(?W..):
    ___  - (self, nukeNode=N.., knob=N.., label='Empty'):
        s_(colorPickerClass, self). - ()
        #window
        resize(QSize(250, 340))
        setStyleSheet(widgetStyle)
        #variables
        nukeNode = nukeNode
        knob = knob
        picker = N..
        #ui
        mainLy = ?VB..
        sL..(mainLy)
        #picker switcher
        lab = ?L..(label)
        mainLy.aW..(lab)
        switch_ly = QHBoxLayout()
        rb1 = QRadioButton()
        rb1.setText('Circle')
        rb1.setChecked(1)
        rb1.c__.c..(addPicker)
        switch_ly.aW..(rb1)
        rb2 = QRadioButton()
        rb2.c__.c..(addPicker)
        rb2.setText('Square')
        switch_ly.aW..(rb2)
        mainLy.addLayout(switch_ly)

        #color swatch
        color = ?L..()
        mainLy.aW..(color)
        ly = QHBoxLayout()
        picker_ly = ?VB..
        picker_ly.setContentsMargins(0,0,0,0)
        ly.addLayout(picker_ly)
        #value
        value = QSlider(Qt.Vertical)
        value.setStyleSheet(sliderStyle)
        value.setMaximumHeight(200)
        ly.aW..(value)
        value.setRange(0,1000)
        value.sV..(1000)
        mainLy.addLayout(ly)
        #color values
        grid_ly = QGridLayout()
        hex_lb = ?L..()
        hex_lb.setLayoutDirection(Qt.RightToLeft)
        hex_lb.setText("HEX")
        grid_ly.aW..(hex_lb, 0, 0, 1, 1)
        hex_le = QLineEdit()
        grid_ly.aW..(hex_le, 0, 1, 1, 1)

        rgb_lb = ?L..()
        rgb_lb.setLayoutDirection(Qt.RightToLeft)
        rgb_lb.setText("RGB")
        grid_ly.aW..(rgb_lb, 1, 0, 1, 1)
        rgb_le = QLineEdit()
        grid_ly.aW..(rgb_le, 1, 1, 1, 1)

        hsv_lb = ?L..()
        hsv_lb.setLayoutDirection(Qt.RightToLeft)
        hsv_lb.setText("HSV")
        grid_ly.aW..(hsv_lb, 2, 0, 1, 1)
        hsv_le = QLineEdit()
        grid_ly.aW..(hsv_le, 2, 1, 1, 1)

        mainLy.addLayout(grid_ly)
        mainLy.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        #START

        addPicker()
        picker.updateColor()

    ___ addPicker
        __ picker:
            picker.setParent(N..)
        __ rb1.isChecked():
            picker = colorWheelClass()
        ____
            picker = colorRampClass()

        picker.colorChangedSignal.c..(receiveColor)
        picker_ly.aW..(picker)
        value.valueChanged.c..(picker.sV..)
        picker.sV..(value.value())
        picker.updateColor()

    ___ setPickerIcon
        pix = QPixmap(32,32)
        pix.fill(QColor(Qt.red))
        setWindowIcon(QIcon(pix))

    ___ receiveColor(self, hs):
        v = value.v..*0.001
        c = QColor()
        c.setHsvF(hs[0], hs[1], v)
        updateColor(c)

    ___ updateColor(self, color):
        color.setStyleSheet('''
        QWidget{
            background-color:%s;
            border-style: solid;
            border: 1px solid #fff;
            border-radius: 2;
        }''' % color.name())
        #hex
        hex_le.setText(color.name())
        #rgb
        rgb_le.setText('%d,%d,%d' % (color.red(), color.green(), color.blue()))
        #hsv
        hsv_le.setText('{0},{1},{2}'.format(*color.getHsv()))
        __ nukeNode:
            knob = nukeNode.knob(knob)
            __ knob:
                knob.sV..([color.red()/255.0, color.green()/255.0, color.blue()/255.0, 1])
            ____
                ?.tprint('%s, %s ' % (knob, knob))



___ addTab(node):
    tab = node.findChild(QTabWidget)
    w = ?W..()
    ly = QHBoxLayout()
    w.sL..(ly)
    cp1 = colorPickerClass(?.toNode(node.objectName()),'shadows.gain', 'Shadows')
    cp2 = colorPickerClass(?.toNode(node.objectName()),'midtones.gain', 'Mid tone')
    cp3 = colorPickerClass(?.toNode(node.objectName()),'highlights.gain', 'Highlights')
    ly.aW..(cp1)
    ly.aW..(cp2)
    ly.aW..(cp3)

    tab.insertTab(0, w, 'Color Wheels')
    tab.setCurrentIndex(0)
    node.resize(777, 670)


__ __name__ __ '__main__':
    app = QApplication([])
    s = colorPickerClass()
    s.s__
    app.exec_()