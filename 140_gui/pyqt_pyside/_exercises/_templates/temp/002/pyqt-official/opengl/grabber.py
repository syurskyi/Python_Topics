#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


______ sys
______ math

____ ?.?C.. ______ pyqtSignal, QSize, __, QTimer
____ ?.?G.. ______ QOpenGLVersionProfile, QPixmap
____ ?.?W.. ______ (?A.., ?A.., QGridLayout, QLabel,
        QLineEdit, QMainWindow, ?MB.., QOpenGLWidget, QScrollArea,
        QSizePolicy, QSlider, QWidget)


c_ GLWidget(QOpenGLWidget):
    xRotationChanged _ pyqtSignal(int)
    yRotationChanged _ pyqtSignal(int)
    zRotationChanged _ pyqtSignal(int)

    ___ __init__  parent_None):
        super(GLWidget, self).__init__(parent)

        self.gear1 _ 0
        self.gear2 _ 0
        self.gear3 _ 0
        self.xRot _ 0
        self.yRot _ 0
        self.zRot _ 0
        self.gear1Rot _ 0

        timer _ QTimer(self)
        timer.timeout.c..(self.advanceGears)
        timer.start(20)

    ___ setXRotation  angle):
        self.normalizeAngle(angle)

        __ angle !_ self.xRot:
            self.xRot _ angle
            self.xRotationChanged.emit(angle)
            self.update()

    ___ setYRotation  angle):
        self.normalizeAngle(angle)

        __ angle !_ self.yRot:
            self.yRot _ angle
            self.yRotationChanged.emit(angle)
            self.update()

    ___ setZRotation  angle):
        self.normalizeAngle(angle)

        __ angle !_ self.zRot:
            self.zRot _ angle
            self.zRotationChanged.emit(angle)
            self.update()

    ___ initializeGL(self):
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl _ self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()

        lightPos _ (5.0, 5.0, 10.0, 1.0)
        reflectance1 _ (0.8, 0.1, 0.0, 1.0)
        reflectance2 _ (0.0, 0.8, 0.2, 1.0)
        reflectance3 _ (0.2, 0.2, 1.0, 1.0)

        self.gl.glLightfv(self.gl.GL_LIGHT0, self.gl.GL_POSITION, lightPos)
        self.gl.glEnable(self.gl.GL_LIGHTING)
        self.gl.glEnable(self.gl.GL_LIGHT0)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)

        self.gear1 _ self.makeGear(reflectance1, 1.0, 4.0, 1.0, 0.7, 20)
        self.gear2 _ self.makeGear(reflectance2, 0.5, 2.0, 2.0, 0.7, 10)
        self.gear3 _ self.makeGear(reflectance3, 1.3, 2.0, 0.5, 0.7, 10)

        self.gl.glEnable(self.gl.GL_NORMALIZE)
        self.gl.glClearColor(0.0, 0.0, 0.0, 1.0)

    ___ paintGL(self):
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)

        self.gl.glPushMatrix()
        self.gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        self.gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        self.gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

        self.drawGear(self.gear1, -3.0, -2.0, 0.0, self.gear1Rot / 16.0)
        self.drawGear(self.gear2, +3.1, -2.0, 0.0,
                -2.0 * (self.gear1Rot / 16.0) - 9.0)

        self.gl.glRotated(+90.0, 1.0, 0.0, 0.0)
        self.drawGear(self.gear3, -3.1, -1.8, -2.2,
                +2.0 * (self.gear1Rot / 16.0) - 2.0)

        self.gl.glPopMatrix()

    ___ resizeGL  width, height):
        side _ min(width, height)
        __ side < 0:
            r_

        self.gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(0.0, 0.0, -40.0)

    ___ mousePressEvent  event):
        self.lastPos _ event.pos()

    ___ mouseMoveEvent  event):
        dx _ event.x() - self.lastPos.x()
        dy _ event.y() - self.lastPos.y()

        __ event.buttons() & __.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        ____ event.buttons() & __.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos _ event.pos()

    ___ advanceGears(self):
        self.gear1Rot +_ 2 * 16
        self.update()    

    ___ xRotation(self):
        r_ self.xRot

    ___ yRotation(self):
        r_ self.yRot

    ___ zRotation(self):
        r_ self.zRot

    ___ makeGear  reflectance, innerRadius, outerRadius, thickness, toothSize, toothCount):
        list _ self.gl.glGenLists(1)
        self.gl.glNewList(list, self.gl.GL_COMPILE)
        self.gl.glMaterialfv(self.gl.GL_FRONT, self.gl.GL_AMBIENT_AND_DIFFUSE,
                reflectance)

        r0 _ innerRadius
        r1 _ outerRadius - toothSize / 2.0
        r2 _ outerRadius + toothSize / 2.0
        delta _ (2.0 * math.pi / toothCount) / 4.0
        z _ thickness / 2.0

        self.gl.glShadeModel(self.gl.GL_FLAT)

        for i in range(2):
            __ i == 0:
                sign _ +1.0
            ____
                sign _ -1.0

            self.gl.glNormal3d(0.0, 0.0, sign)

            self.gl.glBegin(self.gl.GL_QUAD_STRIP)

            for j in range(toothCount+1):
                angle _ 2.0 * math.pi * j / toothCount
                self.gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), sign * z)
                self.gl.glVertex3d(r1 * math.cos(angle), r1 * math.sin(angle), sign * z)
                self.gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), sign * z)
                self.gl.glVertex3d(r1 * math.cos(angle + 3 * delta), r1 * math.sin(angle + 3 * delta), sign * z)

            self.gl.glEnd()

            self.gl.glBegin(self.gl.GL_QUADS)

            for j in range(toothCount):
                angle _ 2.0 * math.pi * j / toothCount
                self.gl.glVertex3d(r1 * math.cos(angle), r1 * math.sin(angle), sign * z)
                self.gl.glVertex3d(r2 * math.cos(angle + delta), r2 * math.sin(angle + delta), sign * z)
                self.gl.glVertex3d(r2 * math.cos(angle + 2 * delta), r2 * math.sin(angle + 2 * delta), sign * z)
                self.gl.glVertex3d(r1 * math.cos(angle + 3 * delta), r1 * math.sin(angle + 3 * delta), sign * z)

            self.gl.glEnd()

        self.gl.glBegin(self.gl.GL_QUAD_STRIP)

        for i in range(toothCount):
            for j in range(2):
                angle _ 2.0 * math.pi * (i + (j / 2.0)) / toothCount
                s1 _ r1
                s2 _ r2

                __ j == 1:
                    s1, s2 _ s2, s1

                self.gl.glNormal3d(math.cos(angle), math.sin(angle), 0.0)
                self.gl.glVertex3d(s1 * math.cos(angle), s1 * math.sin(angle), +z)
                self.gl.glVertex3d(s1 * math.cos(angle), s1 * math.sin(angle), -z)

                self.gl.glNormal3d(s2 * math.sin(angle + delta) - s1 * math.sin(angle), s1 * math.cos(angle) - s2 * math.cos(angle + delta), 0.0)
                self.gl.glVertex3d(s2 * math.cos(angle + delta), s2 * math.sin(angle + delta), +z)
                self.gl.glVertex3d(s2 * math.cos(angle + delta), s2 * math.sin(angle + delta), -z)

        self.gl.glVertex3d(r1, 0.0, +z)
        self.gl.glVertex3d(r1, 0.0, -z)
        self.gl.glEnd()

        self.gl.glShadeModel(self.gl.GL_SMOOTH)

        self.gl.glBegin(self.gl.GL_QUAD_STRIP)

        for i in range(toothCount+1):
            angle _ i * 2.0 * math.pi / toothCount
            self.gl.glNormal3d(-math.cos(angle), -math.sin(angle), 0.0)
            self.gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), +z)
            self.gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), -z)

        self.gl.glEnd()

        self.gl.glEndList()

        r_ list    

    ___ drawGear  gear, dx, dy, dz, angle):
        self.gl.glPushMatrix()
        self.gl.glTranslated(dx, dy, dz)
        self.gl.glRotated(angle, 0.0, 0.0, 1.0)
        self.gl.glCallList(gear)
        self.gl.glPopMatrix()

    ___ normalizeAngle  angle):
        while (angle < 0):
            angle +_ 360 * 16

        while (angle > 360 * 16):
            angle -_ 360 * 16


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        centralWidget _ QWidget()
        self.sCW..(centralWidget)

        self.glWidget _ GLWidget()
        self.pixmapLabel _ QLabel()

        self.glWidgetArea _ QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QSizePolicy.Ignored,
                QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        self.pixmapLabelArea _ QScrollArea()
        self.pixmapLabelArea.setWidget(self.pixmapLabel)
        self.pixmapLabelArea.setSizePolicy(QSizePolicy.Ignored,
                QSizePolicy.Ignored)
        self.pixmapLabelArea.setMinimumSize(50, 50)

        xSlider _ self.createSlider(self.glWidget.xRotationChanged,
                self.glWidget.setXRotation)
        ySlider _ self.createSlider(self.glWidget.yRotationChanged,
                self.glWidget.setYRotation)
        zSlider _ self.createSlider(self.glWidget.zRotationChanged,
                self.glWidget.setZRotation)

        self.createActions()
        self.createMenus()

        centralLayout _ QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralLayout.addWidget(self.pixmapLabelArea, 0, 1)
        centralLayout.addWidget(xSlider, 1, 0, 1, 2)
        centralLayout.addWidget(ySlider, 2, 0, 1, 2)
        centralLayout.addWidget(zSlider, 3, 0, 1, 2)
        centralWidget.setLayout(centralLayout)

        xSlider.setValue(15 * 16)
        ySlider.setValue(345 * 16)
        zSlider.setValue(0 * 16)

        self.setWindowTitle("Grabber")
        self.resize(400, 300)

    ___ grabFrameBuffer(self):
        image _ self.glWidget.grabFramebuffer()
        self.setPixmap(QPixmap.fromImage(image))

    ___ clearPixmap(self):
        self.setPixmap(QPixmap())

    ___ about(self):
        ?MB...about  "About Grabber",
                "The <b>Grabber</b> example demonstrates two approaches for "
                "rendering OpenGL into a Qt pixmap.")

    ___ createActions(self):
        self.grabFrameBufferAct _ ?A..("&Grab Frame Buffer", self,
                shortcut_"Ctrl+G", triggered_self.grabFrameBuffer)

        self.clearPixmapAct _ ?A..("&Clear Pixmap", self,
                shortcut_"Ctrl+L", triggered_self.clearPixmap)

        self.exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.aboutAct _ ?A..("&About", self, triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.grabFrameBufferAct)
        self.fileMenu.aA..(self.clearPixmapAct)
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.exitAct)

        self.helpMenu _ self.mB.. .aM..("&Help")
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

    ___ createSlider  changedSignal, setterSlot):
        slider _ QSlider(__.Horizontal)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)

        slider.valueChanged.c..(setterSlot)
        changedSignal.c..(slider.setValue)

        r_ slider

    ___ setPixmap  pixmap):
        self.pixmapLabel.setPixmap(pixmap)
        size _ pixmap.size()

        __ size - QSize(1, 0) == self.pixmapLabelArea.maximumViewportSize
            size -_ QSize(1, 0)

        self.pixmapLabel.resize(size)


__ __name__ == '__main__':

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())    
