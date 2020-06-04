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

______ m__

____ ?.?C.. ______ pP.., pS.., pyqtSlot, QPoint, ?S.., __
____ ?.?G.. ______ ?C..
____ ?.?W.. ______ ?A.., QOpenGLWidget


c_ HelloGLWidget(QOpenGLWidget):
    """HelloGLWidget(QOpenGLWidget)

    Provides a custom widget to display an OpenGL-rendered Qt logo.
    Various properties and slots are defined so that the user can rotate
    the logo, and signals are defined to enable other components to
    react to changes to its orientation.
    """

    # We define three signals that are used to indicate changes to the
    # rotation of the logo.
    xRotationChanged _ pS..(in.)
    yRotationChanged _ pS..(in.)
    zRotationChanged _ pS..(in.)

    ___  -   parent_None):
        s__(HelloGLWidget, self). - (parent)

        object _ 0
        xRot _ 0
        yRot _ 0
        zRot _ 0

        lastPos _ QPoint()

        trolltechGreen _ ?C...fromCmykF(0.40, 0.0, 1.0, 0.0)
        trolltechPurple _ ?C...fromCmykF(0.39, 0.39, 0.0, 0.0)

        sWT..("Hello GL")

    # The rotation of the logo about the x-axis can be controlled using the
    # xRotation property, defined using the following getter and setter
    # methods.

    ___ getXRotation
        r_ xRot

    # The setXRotation() setter method is also a slot.
    @pyqtSlot(in.)
    ___ setXRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ xRot:
            xRot _ angle
            xRotationChanged.e..(angle)
            update()

    xRotation _ pP..(in., getXRotation, setXRotation)

    # The rotation of the logo about the y-axis can be controlled using the
    # yRotation property, defined using the following getter and setter
    # methods.

    ___ getYRotation
        r_ yRot

    # The setYRotation() setter method is also a slot.
    @pyqtSlot(in.)
    ___ setYRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ yRot:
            yRot _ angle
            yRotationChanged.e..(angle)
            update()

    yRotation _ pP..(in., getYRotation, setYRotation)

    # The rotation of the logo about the z-axis can be controlled using the
    # zRotation property, defined using the following getter and setter
    # methods.

    ___ getZRotation
        r_ zRot

    # The setZRotation() setter method is also a slot.
    @pyqtSlot(in.)
    ___ setZRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ zRot:
            zRot _ angle
            zRotationChanged.e..(angle)
            update()

    zRotation _ pP..(in., getZRotation, setZRotation)

    ___ minimumSizeHint
        r_ ?S..(50, 50)

    ___ sH..
        r_ ?S..(200, 200)

    ___ initializeGL
        gl _ context().versionFunctions()
        gl.initializeOpenGLFunctions()

        setClearColor(trolltechPurple.darker())
        object _ makeObject()
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)

    ___ paintGL
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -10.0)
        gl.glRotated(xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(zRot / 16.0, 0.0, 0.0, 1.0)
        gl.glCallList(object)

    ___ resizeGL  width, height):
        side _ min(width, height)
        gl.glViewport((width - side) / 2, (height - side) / 2, side, side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    ___ mousePressEvent  event):
        lastPos _ QPoint(event.pos())

    ___ mouseMoveEvent  event):
        dx _ event.x() - lastPos.x()
        dy _ event.y() - lastPos.y()

        __ event.buttons() & __.LeftButton:
            setXRotation(xRot + 8 * dy)
            setYRotation(yRot + 8 * dx)
        ____ event.buttons() & __.RightButton:
            setXRotation(xRot + 8 * dy)
            setZRotation(zRot + 8 * dx)

        lastPos _ QPoint(event.pos())

    ___ makeObject
        genList _ gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)

        gl.glBegin(gl.GL_QUADS)

        x1 _ +0.06
        y1 _ -0.14
        x2 _ +0.14
        y2 _ -0.06
        x3 _ +0.08
        y3 _ +0.00
        x4 _ +0.30
        y4 _ +0.22

        quad(x1, y1, x2, y2, y2, x2, y1, x1)
        quad(x3, y3, x4, y4, y4, x4, y3, x3)

        extrude(x1, y1, x2, y2)
        extrude(x2, y2, y2, x2)
        extrude(y2, x2, y1, x1)
        extrude(y1, x1, x1, y1)
        extrude(x3, y3, x4, y4)
        extrude(x4, y4, y4, x4)
        extrude(y4, x4, y3, x3)

        Pi _ 3.14159265358979323846
        NumSectors _ 200

        ___ i __ ra..(NumSectors):
            angle1 _ (i * 2 * Pi) / NumSectors
            x5 _ 0.30 * m__.sin(angle1)
            y5 _ 0.30 * m__.cos(angle1)
            x6 _ 0.20 * m__.sin(angle1)
            y6 _ 0.20 * m__.cos(angle1)

            angle2 _ ((i + 1) * 2 * Pi) / NumSectors
            x7 _ 0.20 * m__.sin(angle2)
            y7 _ 0.20 * m__.cos(angle2)
            x8 _ 0.30 * m__.sin(angle2)
            y8 _ 0.30 * m__.cos(angle2)

            quad(x5, y5, x6, y6, x7, y7, x8, y8)

            extrude(x6, y6, x7, y7)
            extrude(x8, y8, x5, y5)

        gl.glEnd()
        gl.glEndList()

        r_ genList

    ___ quad  x1, y1, x2, y2, x3, y3, x4, y4):
        sC..(trolltechGreen)

        gl.glVertex3d(x1, y1, -0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x3, y3, -0.05)
        gl.glVertex3d(x4, y4, -0.05)

        gl.glVertex3d(x4, y4, +0.05)
        gl.glVertex3d(x3, y3, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x1, y1, +0.05)

    ___ extrude  x1, y1, x2, y2):
        sC..(trolltechGreen.darker(250 + in.(100 * x1)))

        gl.glVertex3d(x1, y1, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x1, y1, -0.05)

    ___ normalizeAngle  angle):
        w__ angle < 0:
            angle +_ 360 * 16
        w__ angle > 360 * 16:
            angle -_ 360 * 16
        r_ angle

    ___ setClearColor  c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    ___ sC..  c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    widget _ HelloGLWidget()
    widget.s..
    ___.e.. ?.e..
