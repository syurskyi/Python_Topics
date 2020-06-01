#!/usr/bin/env python

"""
helloglwidget.py

A simple OpenGL custom widget for Qt Designer.

Copyright (C) 2007 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

______ math

____ ?.QtCore ______ pyqtProperty, pyqtSignal, pyqtSlot, QPoint, QSize, Qt
____ ?.QtGui ______ QColor
____ ?.?W.. ______ ?A.., QOpenGLWidget


class HelloGLWidget(QOpenGLWidget):
    """HelloGLWidget(QOpenGLWidget)

    Provides a custom widget to display an OpenGL-rendered Qt logo.
    Various properties and slots are defined so that the user can rotate
    the logo, and signals are defined to enable other components to
    react to changes to its orientation.
    """

    # We define three signals that are used to indicate changes to the
    # rotation of the logo.
    xRotationChanged _ pyqtSignal(int)
    yRotationChanged _ pyqtSignal(int)
    zRotationChanged _ pyqtSignal(int)

    ___ __init__(self, parent_None):
        super(HelloGLWidget, self).__init__(parent)

        self.object _ 0
        self.xRot _ 0
        self.yRot _ 0
        self.zRot _ 0

        self.lastPos _ QPoint()

        self.trolltechGreen _ QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple _ QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

        self.setWindowTitle("Hello GL")

    # The rotation of the logo about the x-axis can be controlled using the
    # xRotation property, defined using the following getter and setter
    # methods.

    ___ getXRotation(self):
        return self.xRot

    # The setXRotation() setter method is also a slot.
    @pyqtSlot(int)
    ___ setXRotation(self, angle):
        angle _ self.normalizeAngle(angle)
        if angle !_ self.xRot:
            self.xRot _ angle
            self.xRotationChanged.emit(angle)
            self.update()

    xRotation _ pyqtProperty(int, getXRotation, setXRotation)

    # The rotation of the logo about the y-axis can be controlled using the
    # yRotation property, defined using the following getter and setter
    # methods.

    ___ getYRotation(self):
        return self.yRot

    # The setYRotation() setter method is also a slot.
    @pyqtSlot(int)
    ___ setYRotation(self, angle):
        angle _ self.normalizeAngle(angle)
        if angle !_ self.yRot:
            self.yRot _ angle
            self.yRotationChanged.emit(angle)
            self.update()

    yRotation _ pyqtProperty(int, getYRotation, setYRotation)

    # The rotation of the logo about the z-axis can be controlled using the
    # zRotation property, defined using the following getter and setter
    # methods.

    ___ getZRotation(self):
        return self.zRot

    # The setZRotation() setter method is also a slot.
    @pyqtSlot(int)
    ___ setZRotation(self, angle):
        angle _ self.normalizeAngle(angle)
        if angle !_ self.zRot:
            self.zRot _ angle
            self.zRotationChanged.emit(angle)
            self.update()

    zRotation _ pyqtProperty(int, getZRotation, setZRotation)

    ___ minimumSizeHint(self):
        return QSize(50, 50)

    ___ sizeHint(self):
        return QSize(200, 200)

    ___ initializeGL(self):
        self.gl _ self.context().versionFunctions()
        self.gl.initializeOpenGLFunctions()

        self.setClearColor(self.trolltechPurple.darker())
        self.object _ self.makeObject()
        self.gl.glShadeModel(self.gl.GL_SMOOTH)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_CULL_FACE)

    ___ paintGL(self):
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(0.0, 0.0, -10.0)
        self.gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        self.gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        self.gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        self.gl.glCallList(self.object)

    ___ resizeGL(self, width, height):
        side _ min(width, height)
        self.gl.glViewport((width - side) / 2, (height - side) / 2, side, side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    ___ mousePressEvent(self, event):
        self.lastPos _ QPoint(event.pos())

    ___ mouseMoveEvent(self, event):
        dx _ event.x() - self.lastPos.x()
        dy _ event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos _ QPoint(event.pos())

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

        Pi _ 3.14159265358979323846
        NumSectors _ 200

        for i in range(NumSectors):
            angle1 _ (i * 2 * Pi) / NumSectors
            x5 _ 0.30 * math.sin(angle1)
            y5 _ 0.30 * math.cos(angle1)
            x6 _ 0.20 * math.sin(angle1)
            y6 _ 0.20 * math.cos(angle1)

            angle2 _ ((i + 1) * 2 * Pi) / NumSectors
            x7 _ 0.20 * math.sin(angle2)
            y7 _ 0.20 * math.cos(angle2)
            x8 _ 0.30 * math.sin(angle2)
            y8 _ 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        self.gl.glEnd()
        self.gl.glEndList()

        return genList

    ___ quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.setColor(self.trolltechGreen)

        self.gl.glVertex3d(x1, y1, -0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x3, y3, -0.05)
        self.gl.glVertex3d(x4, y4, -0.05)

        self.gl.glVertex3d(x4, y4, +0.05)
        self.gl.glVertex3d(x3, y3, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x1, y1, +0.05)

    ___ extrude(self, x1, y1, x2, y2):
        self.setColor(self.trolltechGreen.darker(250 + int(100 * x1)))

        self.gl.glVertex3d(x1, y1, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x1, y1, -0.05)

    ___ normalizeAngle(self, angle):
        while angle < 0:
            angle +_ 360 * 16
        while angle > 360 * 16:
            angle -_ 360 * 16
        return angle

    ___ setClearColor(self, c):
        self.gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    ___ setColor(self, c):
        self.gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


if __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)
    widget _ HelloGLWidget()
    widget.s..
    sys.exit(app.exec_())
