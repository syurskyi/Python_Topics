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

____ ?.?C.. ______ pyqtSignal, QPoint, QSize, __
____ ?.?G.. ______ ?C.., QOpenGLVersionProfile
____ ?.?W.. ______ (?A.., QHBoxLayout, QOpenGLWidget, QSlider,
        QWidget)


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.glWidget _ GLWidget()

        self.xSlider _ self.createSlider()
        self.ySlider _ self.createSlider()
        self.zSlider _ self.createSlider()

        self.xSlider.valueChanged.c..(self.glWidget.setXRotation)
        self.glWidget.xRotationChanged.c..(self.xSlider.setValue)
        self.ySlider.valueChanged.c..(self.glWidget.setYRotation)
        self.glWidget.yRotationChanged.c..(self.ySlider.setValue)
        self.zSlider.valueChanged.c..(self.glWidget.setZRotation)
        self.glWidget.zRotationChanged.c..(self.zSlider.setValue)

        mainLayout _ QHBoxLayout()
        mainLayout.addWidget(self.glWidget)
        mainLayout.addWidget(self.xSlider)
        mainLayout.addWidget(self.ySlider)
        mainLayout.addWidget(self.zSlider)
        self.setLayout(mainLayout)

        self.xSlider.setValue(15 * 16)
        self.ySlider.setValue(345 * 16)
        self.zSlider.setValue(0 * 16)

        self.setWindowTitle("Hello GL")

    ___ createSlider(self):
        slider _ QSlider(__.Vertical)

        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)

        r_ slider


c_ GLWidget(QOpenGLWidget):
    xRotationChanged _ pyqtSignal(int)
    yRotationChanged _ pyqtSignal(int)
    zRotationChanged _ pyqtSignal(int)

    ___ __init__  parent_None):
        super(GLWidget, self).__init__(parent)

        self.object _ 0
        self.xRot _ 0
        self.yRot _ 0
        self.zRot _ 0

        self.lastPos _ QPoint()

        self.trolltechGreen _ ?C...fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple _ ?C...fromCmykF(0.39, 0.39, 0.0, 0.0)

    ___ minimumSizeHint(self):
        r_ QSize(50, 50)

    ___ sizeHint(self):
        r_ QSize(400, 400)

    ___ setXRotation  angle):
        angle _ self.normalizeAngle(angle)
        __ angle !_ self.xRot:
            self.xRot _ angle
            self.xRotationChanged.emit(angle)
            self.update()

    ___ setYRotation  angle):
        angle _ self.normalizeAngle(angle)
        __ angle !_ self.yRot:
            self.yRot _ angle
            self.yRotationChanged.emit(angle)
            self.update()

    ___ setZRotation  angle):
        angle _ self.normalizeAngle(angle)
        __ angle !_ self.zRot:
            self.zRot _ angle
            self.zRotationChanged.emit(angle)
            self.update()

    ___ initializeGL(self):
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl _ self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()

        self.setClearColor(self.trolltechPurple.darker())
        self.object _ self.makeObject()
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_CULL_FACE)

    ___ paintGL(self):
        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(0.0, 0.0, -10.0)
        self.gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        self.gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        self.gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        self.gl.glCallList(self.object)

    ___ resizeGL  width, height):
        side _ min(width, height)
        __ side < 0:
            r_

        self.gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

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

    ___ makeObject(self):
        genList _ self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glBegin(self.gl.GL_QUADS)

        x1 _ +0.06
        y1 _ -0.14
        x2 _ +0.14
        y2 _ -0.06
        x3 _ +0.08
        y3 _ +0.00
        x4 _ +0.30
        y4 _ +0.22

        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        NumSectors _ 200

        for i in range(NumSectors):
            angle1 _ (i * 2 * math.pi) / NumSectors
            x5 _ 0.30 * math.sin(angle1)
            y5 _ 0.30 * math.cos(angle1)
            x6 _ 0.20 * math.sin(angle1)
            y6 _ 0.20 * math.cos(angle1)

            angle2 _ ((i + 1) * 2 * math.pi) / NumSectors
            x7 _ 0.20 * math.sin(angle2)
            y7 _ 0.20 * math.cos(angle2)
            x8 _ 0.30 * math.sin(angle2)
            y8 _ 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        self.gl.glEnd()
        self.gl.glEndList()

        r_ genList

    ___ quad  x1, y1, x2, y2, x3, y3, x4, y4):
        self.sC..(self.trolltechGreen)

        self.gl.glVertex3d(x1, y1, -0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x3, y3, -0.05)
        self.gl.glVertex3d(x4, y4, -0.05)

        self.gl.glVertex3d(x4, y4, +0.05)
        self.gl.glVertex3d(x3, y3, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x1, y1, +0.05)

    ___ extrude  x1, y1, x2, y2):
        self.sC..(self.trolltechGreen.darker(250 + int(100 * x1)))

        self.gl.glVertex3d(x1, y1, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x1, y1, -0.05)

    ___ normalizeAngle  angle):
        while angle < 0:
            angle +_ 360 * 16
        while angle > 360 * 16:
            angle -_ 360 * 16
        r_ angle

    ___ setClearColor  c):
        self.gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    ___ sC..  c):
        self.gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


__ __name__ == '__main__':

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
