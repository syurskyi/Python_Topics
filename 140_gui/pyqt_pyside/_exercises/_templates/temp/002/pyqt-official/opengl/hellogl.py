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


______ ___
______ m__

____ ?.?C.. ______ pS.., QPoint, ?S.., __
____ ?.?G.. ______ ?C.., QOpenGLVersionProfile
____ ?.?W.. ______ (?A.., ?HBL.., QOpenGLWidget, ?S..,
        ?W..)


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        glWidget _ GLWidget()

        xSlider _ createSlider()
        ySlider _ createSlider()
        zSlider _ createSlider()

        xSlider.valueChanged.c..(glWidget.setXRotation)
        glWidget.xRotationChanged.c..(xSlider.sV..)
        ySlider.valueChanged.c..(glWidget.setYRotation)
        glWidget.yRotationChanged.c..(ySlider.sV..)
        zSlider.valueChanged.c..(glWidget.setZRotation)
        glWidget.zRotationChanged.c..(zSlider.sV..)

        mainLayout _ ?HBL..
        mainLayout.aW..(glWidget)
        mainLayout.aW..(xSlider)
        mainLayout.aW..(ySlider)
        mainLayout.aW..(zSlider)
        sL..(mainLayout)

        xSlider.sV..(15 * 16)
        ySlider.sV..(345 * 16)
        zSlider.sV..(0 * 16)

        sWT..("Hello GL")

    ___ createSlider
        slider _ ?S..(__.Vertical)

        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(?S...TicksRight)

        r_ slider


c_ GLWidget(QOpenGLWidget):
    xRotationChanged _ pS..(in.)
    yRotationChanged _ pS..(in.)
    zRotationChanged _ pS..(in.)

    ___  -   parent_None):
        s__(GLWidget, self). - (parent)

        object _ 0
        xRot _ 0
        yRot _ 0
        zRot _ 0

        lastPos _ QPoint()

        trolltechGreen _ ?C...fromCmykF(0.40, 0.0, 1.0, 0.0)
        trolltechPurple _ ?C...fromCmykF(0.39, 0.39, 0.0, 0.0)

    ___ minimumSizeHint
        r_ ?S..(50, 50)

    ___ sH..
        r_ ?S..(400, 400)

    ___ setXRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ xRot:
            xRot _ angle
            xRotationChanged.e..(angle)
            update()

    ___ setYRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ yRot:
            yRot _ angle
            yRotationChanged.e..(angle)
            update()

    ___ setZRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ zRot:
            zRot _ angle
            zRotationChanged.e..(angle)
            update()

    ___ initializeGL
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        gl _ context().versionFunctions(version_profile)
        gl.initializeOpenGLFunctions()

        setClearColor(trolltechPurple.darker())
        object _ makeObject()
        gl.glShadeModel(gl.GL_FLAT)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)

    ___ paintGL
        gl.glClear(
                gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -10.0)
        gl.glRotated(xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(zRot / 16.0, 0.0, 0.0, 1.0)
        gl.glCallList(object)

    ___ resizeGL  width, height):
        side _ min(width, height)
        __ side < 0:
            r_

        gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    ___ mousePressEvent  event):
        lastPos _ event.pos()

    ___ mouseMoveEvent  event):
        dx _ event.x() - lastPos.x()
        dy _ event.y() - lastPos.y()

        __ event.buttons() & __.LeftButton:
            setXRotation(xRot + 8 * dy)
            setYRotation(yRot + 8 * dx)
        ____ event.buttons() & __.RightButton:
            setXRotation(xRot + 8 * dy)
            setZRotation(zRot + 8 * dx)

        lastPos _ event.pos()

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

        NumSectors _ 200

        ___ i __ ra..(NumSectors):
            angle1 _ (i * 2 * m__.pi) / NumSectors
            x5 _ 0.30 * m__.sin(angle1)
            y5 _ 0.30 * m__.cos(angle1)
            x6 _ 0.20 * m__.sin(angle1)
            y6 _ 0.20 * m__.cos(angle1)

            angle2 _ ((i + 1) * 2 * m__.pi) / NumSectors
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


__ ______ __ ______

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
