____ ?.?C.. ______ _
____ ?.?G.. ______ _

______ math
___
    ______ ?
______pass

sliderStyle _ '''QSlider::groove:vertical {
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
widgetStyle _ '''
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
    colorChangedSignal _ Signal(list)
    ___  -
        s_(colorWheelClass, self). - ()
        hw _ 200
        padding _ 2
        blackBorder _ 10
        radius _ (hw / 2) - padding
        center _ hw / 2
        setFixedSize(QSize(hw, hw))
        img _ N..
        pick _ [0, 0]
        pickerSize _ 8
        v..  _ 0

    ___ paintEvent(self, event):
        __ no. img:
            img _ getCircle()
        painter _ QPainter()
        painter.begin(self)
        #wheel
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawImage(0, 0, img)
        #value
        painter.setPen(__.NoPen)
        elipse _ QPainterPath()
        elipse.addEllipse(QRect(blackBorder, blackBorder, hw-blackBorder*2,hw-blackBorder*2))
        painter.setBrush(QColor(0,0,0,v.. *255))
        painter.drawPath(elipse)


        #picker
        x _ center + pick[0]
        y _ center + pick[1]
        #line
        painter.setBrush(__.NoBrush)
        lineColor _ 55 __ v..  < 0.5 ____ 200
        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 1))
        painter.drawLine(center, center,x, y)

        painter.setPen(QPen(QColor(lineColor,lineColor,lineColor), 1, __.DashLine))
        size _ math.sqrt((pick[0] * pick[0]) + (pick[1] * pick[1]))
        painter.drawEllipse(center-size,
                            center-size,
                            size*2,
                            size*2)
        #decorate
        painter.setPen(QPen(QColor(255,255,255), 3))
        c1 _ padding
        c2 _ hw - padding*2
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
        x _ pos.x()-center
        y _ pos.y() - center
        distance _ math.sqrt((x * x) + (y * y))
        __ distance < radius:
            pick _ [x, y]
            update()
        ____
            over _ radius / distance
            pick _ [x*over, y*over]
            update()
        updateColor()

    ___ updateColor
        x _ pick[0]
        y _ pick[1]
        distance _ math.sqrt((x * x) + (y * y))
        angle _ math.degrees(math.atan2(y,x))
        __ angle < 0:
            angle +_ 360
        s _ min(1, distance / radius)
        colorChangedSignal.emit([angle/360,s])

    ___ sV..(self, v):
        v..  _ (1000-v) * 0.001
        update()
        updateColor()

    ___ getCircle
        img _ QImage(hw, hw, QImage.Format_ARGB32)

        color _ QColor()
        ___ y __ ra..(-center, center):
            ___ x __ ra..(-center, center):
                distance _ math.sqrt((x * x) + (y * y))
                __ distance > radius:
                    color.setRgb(0.0, 0.0, 0.0)
                    color.setAlpha(0.0)
                ____
                    s _ distance / radius
                    angle _ (math.atan2(y, x) * 180 / math.pi)
                    __ y < 0:
                        angle +_ 360
                    h _ angle / 360.0
                    v _ 1
                    color.setHsvF(h, s, v, 1.0)
                img.setPixel(x+center, y+center, color.rgba())
        r_ img


c_ colorRampClass(?W..):
    colorChangedSignal _ Signal(list)
    ___  -
        s_(colorRampClass, self). - ()
        hw _ 200
        setFixedSize(QSize(hw, hw))
        padding _ 2
        v..  _ 0.0
        pick _ [0, 0]
        img _ N..
        pickerSize _ 8

    ___ paintEvent(self, event):
        __ no. img:
            img _ getRamp()
        painter _ QPainter()
        painter.begin(self)
        #wheel
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawImage(0, 0, img)
        #value
        painter.setPen(__.NoPen)
        painter.fillRect(0,0, hw, hw, QColor(0,0,0,v.. *255))
        #lines
        x _ pick[0]
        y _ pick[1]
        lineColor _ 55 __ v..  < 0.5 ____ 200
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
        h _ pick[0]/float(hw)
        s _ pick[1]/float(hw)
        colorChangedSignal.emit([h,s])

    ___ sV..(self, v):
        v..  _ (1000-v) * 0.001
        update()
        updateColor()

    ___ mousePressEvent(self, event):
        setPickerPos(event.pos())
        ?W...mousePressEvent(self, event)

    ___ mouseMoveEvent(self, event):
        setPickerPos(event.pos())
        ?W...mouseMoveEvent(self, event)

    ___ setPickerPos(self, pos):
        x _ pos.x()
        y _ pos.y()
        __ x < 0:
            x _ 0
        __ x > hw:
            x _ hw
        __ y < 0:
            y _ 0
        __ y > hw:
            y _ hw
        pick _ [x, y]
        update()
        updateColor()

    ___ getRamp
        img _ QImage(hw, hw, QImage.Format_RGB32)
        color _ QColor()
        ___ y __ ra..(hw):
            ___ x __ ra..(hw):
                h _ x / float(hw)
                s _ y/ float(hw)
                color.setHsvF(h, s, 1)
                img.setPixel(x, y, color.rgb())
        r_ img


c_ colorPickerClass(?W..):
    ___  - (self, nukeNode_N.., knob_N.., label_'Empty'):
        s_(colorPickerClass, self). - ()
        #window
        resize(QSize(250, 340))
        setStyleSheet(widgetStyle)
        #variables
        nukeNode _ nukeNode
        knob _ knob
        picker _ N..
        #ui
        mainLy _ ?VB..
        sL..(mainLy)
        #picker switcher
        lab _ ?L..(label)
        mainLy.aW..(lab)
        switch_ly _ QHBoxLayout()
        rb1 _ QRadioButton()
        rb1.setText('Circle')
        rb1.setChecked(1)
        rb1.c__.c..(addPicker)
        switch_ly.aW..(rb1)
        rb2 _ QRadioButton()
        rb2.c__.c..(addPicker)
        rb2.setText('Square')
        switch_ly.aW..(rb2)
        mainLy.addLayout(switch_ly)

        #color swatch
        color _ ?L..()
        mainLy.aW..(color)
        ly _ QHBoxLayout()
        picker_ly _ ?VB..
        picker_ly.setContentsMargins(0,0,0,0)
        ly.addLayout(picker_ly)
        #value
        v..  _ QSlider(__.Vertical)
        v.. .setStyleSheet(sliderStyle)
        v.. .setMaximumHeight(200)
        ly.aW..(v.. )
        v.. .setRange(0,1000)
        v.. .sV..(1000)
        mainLy.addLayout(ly)
        #color values
        grid_ly _ QGridLayout()
        hex_lb _ ?L..()
        hex_lb.setLayoutDirection(__.RightToLeft)
        hex_lb.setText("HEX")
        grid_ly.aW..(hex_lb, 0, 0, 1, 1)
        hex_le _ QLineEdit()
        grid_ly.aW..(hex_le, 0, 1, 1, 1)

        rgb_lb _ ?L..()
        rgb_lb.setLayoutDirection(__.RightToLeft)
        rgb_lb.setText("RGB")
        grid_ly.aW..(rgb_lb, 1, 0, 1, 1)
        rgb_le _ QLineEdit()
        grid_ly.aW..(rgb_le, 1, 1, 1, 1)

        hsv_lb _ ?L..()
        hsv_lb.setLayoutDirection(__.RightToLeft)
        hsv_lb.setText("HSV")
        grid_ly.aW..(hsv_lb, 2, 0, 1, 1)
        hsv_le _ QLineEdit()
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
            picker _ colorWheelClass()
        ____
            picker _ colorRampClass()

        picker.colorChangedSignal.c..(receiveColor)
        picker_ly.aW..(picker)
        v.. .valueChanged.c..(picker.sV..)
        picker.sV..(v.. .v.. ())
        picker.updateColor()

    ___ setPickerIcon
        pix _ QPixmap(32,32)
        pix.fill(QColor(__.red))
        setWindowIcon(QIcon(pix))

    ___ receiveColor(self, hs):
        v _ v.. .v..*0.001
        c _ QColor()
        c.setHsvF(hs[0], hs[1], v)
        updateColor(c)

    ___ updateColor(self, color):
        color.setStyleSheet('''
        QWidget{
            background-color:@;
            border-style: solid;
            border: 1px solid #fff;
            border-radius: 2;
        }''' % color.n..
        #hex
        hex_le.setText(color.n..
        #rgb
        rgb_le.setText('%d,%d,%d' % (color.red(), color.green(), color.blue()))
        #hsv
        hsv_le.setText('{0},{1},{2}'.f..(*color.getHsv()))
        __ nukeNode:
            knob _ nukeNode.knob(knob)
            __ knob:
                knob.sV..([color.red()/255.0, color.green()/255.0, color.blue()/255.0, 1])
            ____
                ?.tprint('@, @ ' % (knob, knob))



___ addTab(node):
    tab _ node.fC..(?TW..)
    w _ ?W..()
    ly _ QHBoxLayout()
    w.sL..(ly)
    cp1 _ colorPickerClass(?.tN..(node.objectName()),'shadows.gain', 'Shadows')
    cp2 _ colorPickerClass(?.tN..(node.objectName()),'midtones.gain', 'Mid tone')
    cp3 _ colorPickerClass(?.tN..(node.objectName()),'highlights.gain', 'Highlights')
    ly.aW..(cp1)
    ly.aW..(cp2)
    ly.aW..(cp3)

    tab.insertTab(0, w, 'Color Wheels')
    tab.setCurrentIndex(0)
    node.resize(777, 670)


__ __name__ __ '__main__':
    app _ ?A..(# list)
    s _ colorPickerClass()
    s.s__
    app.exec_()