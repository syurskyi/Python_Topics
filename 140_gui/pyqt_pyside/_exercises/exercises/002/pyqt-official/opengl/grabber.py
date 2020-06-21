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

____ ?.?C.. ______ pS.., ?S.., __, ?T..
____ ?.?G.. ______ QOpenGLVersionProfile, ?P..
____ ?.?W.. ______ (?A.., ?A.., QGridLayout, ?L..,
        QLineEdit, ?MW.., ?MB.., QOpenGLWidget, QScrollArea,
        ?SP.., ?S.., ?W..)


c_ GLWidget(QOpenGLWidget):
    xRotationChanged _ pS..(in.)
    yRotationChanged _ pS..(in.)
    zRotationChanged _ pS..(in.)

    ___  -   parent_None):
        s__(GLWidget, self). - (parent)

        gear1 _ 0
        gear2 _ 0
        gear3 _ 0
        xRot _ 0
        yRot _ 0
        zRot _ 0
        gear1Rot _ 0

        timer _ ?T..
        timer.timeout.c..(advanceGears)
        timer.start(20)

    ___ setXRotation  angle):
        normalizeAngle(angle)

        __ angle !_ xRot:
            xRot _ angle
            xRotationChanged.e..(angle)
            update()

    ___ setYRotation  angle):
        normalizeAngle(angle)

        __ angle !_ yRot:
            yRot _ angle
            yRotationChanged.e..(angle)
            update()

    ___ setZRotation  angle):
        normalizeAngle(angle)

        __ angle !_ zRot:
            zRot _ angle
            zRotationChanged.e..(angle)
            update()

    ___ initializeGL
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        gl _ context().versionFunctions(version_profile)
        gl.initializeOpenGLFunctions()

        lightPos _ (5.0, 5.0, 10.0, 1.0)
        reflectance1 _ (0.8, 0.1, 0.0, 1.0)
        reflectance2 _ (0.0, 0.8, 0.2, 1.0)
        reflectance3 _ (0.2, 0.2, 1.0, 1.0)

        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPos)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glEnable(gl.GL_DEPTH_TEST)

        gear1 _ makeGear(reflectance1, 1.0, 4.0, 1.0, 0.7, 20)
        gear2 _ makeGear(reflectance2, 0.5, 2.0, 2.0, 0.7, 10)
        gear3 _ makeGear(reflectance3, 1.3, 2.0, 0.5, 0.7, 10)

        gl.glEnable(gl.GL_NORMALIZE)
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)

    ___ paintGL
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glPushMatrix()
        gl.glRotated(xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(zRot / 16.0, 0.0, 0.0, 1.0)

        drawGear(gear1, -3.0, -2.0, 0.0, gear1Rot / 16.0)
        drawGear(gear2, +3.1, -2.0, 0.0,
                -2.0 * (gear1Rot / 16.0) - 9.0)

        gl.glRotated(+90.0, 1.0, 0.0, 0.0)
        drawGear(gear3, -3.1, -1.8, -2.2,
                +2.0 * (gear1Rot / 16.0) - 2.0)

        gl.glPopMatrix()

    ___ resizeGL  width, height):
        side _ min(width, height)
        __ side < 0:
            r_

        gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -40.0)

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

    ___ advanceGears
        gear1Rot +_ 2 * 16
        update()

    ___ xRotation
        r_ xRot

    ___ yRotation
        r_ yRot

    ___ zRotation
        r_ zRot

    ___ makeGear  reflectance, innerRadius, outerRadius, thickness, toothSize, toothCount):
        li.. _ gl.glGenLists(1)
        gl.glNewList(li.., gl.GL_COMPILE)
        gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT_AND_DIFFUSE,
                reflectance)

        r0 _ innerRadius
        r1 _ outerRadius - toothSize / 2.0
        r2 _ outerRadius + toothSize / 2.0
        delta _ (2.0 * m__.pi / toothCount) / 4.0
        z _ thickness / 2.0

        gl.glShadeModel(gl.GL_FLAT)

        ___ i __ ra..(2):
            __ i __ 0:
                sign _ +1.0
            ____
                sign _ -1.0

            gl.glNormal3d(0.0, 0.0, sign)

            gl.glBegin(gl.GL_QUAD_STRIP)

            ___ j __ ra..(toothCount+1):
                angle _ 2.0 * m__.pi * j / toothCount
                gl.glVertex3d(r0 * m__.cos(angle), r0 * m__.sin(angle), sign * z)
                gl.glVertex3d(r1 * m__.cos(angle), r1 * m__.sin(angle), sign * z)
                gl.glVertex3d(r0 * m__.cos(angle), r0 * m__.sin(angle), sign * z)
                gl.glVertex3d(r1 * m__.cos(angle + 3 * delta), r1 * m__.sin(angle + 3 * delta), sign * z)

            gl.glEnd()

            gl.glBegin(gl.GL_QUADS)

            ___ j __ ra..(toothCount):
                angle _ 2.0 * m__.pi * j / toothCount
                gl.glVertex3d(r1 * m__.cos(angle), r1 * m__.sin(angle), sign * z)
                gl.glVertex3d(r2 * m__.cos(angle + delta), r2 * m__.sin(angle + delta), sign * z)
                gl.glVertex3d(r2 * m__.cos(angle + 2 * delta), r2 * m__.sin(angle + 2 * delta), sign * z)
                gl.glVertex3d(r1 * m__.cos(angle + 3 * delta), r1 * m__.sin(angle + 3 * delta), sign * z)

            gl.glEnd()

        gl.glBegin(gl.GL_QUAD_STRIP)

        ___ i __ ra..(toothCount):
            ___ j __ ra..(2):
                angle _ 2.0 * m__.pi * (i + (j / 2.0)) / toothCount
                s1 _ r1
                s2 _ r2

                __ j __ 1:
                    s1, s2 _ s2, s1

                gl.glNormal3d(m__.cos(angle), m__.sin(angle), 0.0)
                gl.glVertex3d(s1 * m__.cos(angle), s1 * m__.sin(angle), +z)
                gl.glVertex3d(s1 * m__.cos(angle), s1 * m__.sin(angle), -z)

                gl.glNormal3d(s2 * m__.sin(angle + delta) - s1 * m__.sin(angle), s1 * m__.cos(angle) - s2 * m__.cos(angle + delta), 0.0)
                gl.glVertex3d(s2 * m__.cos(angle + delta), s2 * m__.sin(angle + delta), +z)
                gl.glVertex3d(s2 * m__.cos(angle + delta), s2 * m__.sin(angle + delta), -z)

        gl.glVertex3d(r1, 0.0, +z)
        gl.glVertex3d(r1, 0.0, -z)
        gl.glEnd()

        gl.glShadeModel(gl.GL_SMOOTH)

        gl.glBegin(gl.GL_QUAD_STRIP)

        ___ i __ ra..(toothCount+1):
            angle _ i * 2.0 * m__.pi / toothCount
            gl.glNormal3d(-m__.cos(angle), -m__.sin(angle), 0.0)
            gl.glVertex3d(r0 * m__.cos(angle), r0 * m__.sin(angle), +z)
            gl.glVertex3d(r0 * m__.cos(angle), r0 * m__.sin(angle), -z)

        gl.glEnd()

        gl.glEndList()

        r_ li..

    ___ drawGear  gear, dx, dy, dz, angle):
        gl.glPushMatrix()
        gl.glTranslated(dx, dy, dz)
        gl.glRotated(angle, 0.0, 0.0, 1.0)
        gl.glCallList(gear)
        gl.glPopMatrix()

    ___ normalizeAngle  angle):
        w__ (angle < 0):
            angle +_ 360 * 16

        w__ (angle > 360 * 16):
            angle -_ 360 * 16


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        centralWidget _ ?W..
        sCW..(centralWidget)

        glWidget _ GLWidget()
        pixmapLabel _ ?L..

        glWidgetArea _ QScrollArea()
        glWidgetArea.setWidget(glWidget)
        glWidgetArea.setWidgetResizable( st.
        glWidgetArea.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        glWidgetArea.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        glWidgetArea.sSP..(?SP...Ignored,
                ?SP...Ignored)
        glWidgetArea.sMS..(50, 50)

        pixmapLabelArea _ QScrollArea()
        pixmapLabelArea.setWidget(pixmapLabel)
        pixmapLabelArea.sSP..(?SP...Ignored,
                ?SP...Ignored)
        pixmapLabelArea.sMS..(50, 50)

        xSlider _ createSlider(glWidget.xRotationChanged,
                glWidget.setXRotation)
        ySlider _ createSlider(glWidget.yRotationChanged,
                glWidget.setYRotation)
        zSlider _ createSlider(glWidget.zRotationChanged,
                glWidget.setZRotation)

        createActions()
        createMenus()

        centralLayout _ QGridLayout()
        centralLayout.aW..(glWidgetArea, 0, 0)
        centralLayout.aW..(pixmapLabelArea, 0, 1)
        centralLayout.aW..(xSlider, 1, 0, 1, 2)
        centralLayout.aW..(ySlider, 2, 0, 1, 2)
        centralLayout.aW..(zSlider, 3, 0, 1, 2)
        centralWidget.sL..(centralLayout)

        xSlider.sV..(15 * 16)
        ySlider.sV..(345 * 16)
        zSlider.sV..(0 * 16)

        sWT..("Grabber")
        r..(400, 300)

    ___ grabFrameBuffer
        image _ glWidget.grabFramebuffer()
        sP..(?P...fromImage(image))

    ___ clearPixmap
        sP..(?P..())

    ___ about
        ?MB...about  "About Grabber",
                "The <b>Grabber</b> example demonstrates two approaches for "
                "rendering OpenGL into a Qt pixmap.")

    ___ createActions
        grabFrameBufferAct _ ?A..("&Grab Frame Buffer", self,
                shortcut_"Ctrl+G", triggered_self.grabFrameBuffer)

        clearPixmapAct _ ?A..("&Clear Pixmap", self,
                shortcut_"Ctrl+L", triggered_self.clearPixmap)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(grabFrameBufferAct)
        fileMenu.aA..(clearPixmapAct)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ createSlider  changedSignal, setterSlot):
        slider _ ?S..(__.H..)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(?S...TicksRight)

        slider.valueChanged.c..(setterSlot)
        changedSignal.c..(slider.sV..)

        r_ slider

    ___ sP..  pixmap):
        pixmapLabel.sP..(pixmap)
        size _ pixmap.size()

        __ size - ?S..(1, 0) __ pixmapLabelArea.maximumViewportSize
            size -_ ?S..(1, 0)

        pixmapLabel.r..(size)


__ ______ __ ______

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
