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
______ m__, random

____ ?.?C.. ______ (QPoint, QPointF, QRect, QRectF, ?S.., __, ?T..,
        ?T..)
____ ?.?G.. ______ (?B.., ?C.., QFontMetrics, QImage,
        QOpenGLVersionProfile, QPainter, QRadialGradient, QSurfaceFormat)
____ ?.?W.. ______ ?A.., QOpenGLWidget


c_ Bubble o..
    ___  -   position, radius, velocity):
        position _ position
        vel _ velocity
        radius _ radius

        innerColor _ randomColor()
        outerColor _ randomColor()
        updateBrush()

    ___ updateBrush 
        gradient _ QRadialGradient(QPointF(radius, radius),
                radius, QPointF(radius*0.5, radius*0.5))

        gradient.setColorAt(0, ?C..(255, 255, 255, 255))
        gradient.setColorAt(0.25, innerColor)
        gradient.setColorAt(1, outerColor)
        brush _ ?B..(gradient)

    ___ drawBubble  painter):
        painter.save()
        painter.translate(position.x() - radius,
                position.y() - radius)
        painter.sB..(brush)
        painter.drawEllipse(0, 0, in.(2*radius), in.(2*radius))
        painter.restore()

    ___ randomColor 
        red _ random.randrange(205, 256)
        green _ random.randrange(205, 256)
        blue _ random.randrange(205, 256)
        alpha _ random.randrange(91, 192)

        r_ ?C..(red, green, blue, alpha)

    ___ move  bbox):
        position +_ vel
        leftOverflow _ position.x() - radius - bbox.left()
        rightOverflow _ position.x() + radius - bbox.right()
        topOverflow _ position.y() - radius - bbox.top()
        bottomOverflow _ position.y() + radius - bbox.bottom()

        __ leftOverflow < 0.0:
            position.setX(position.x() - 2 * leftOverflow)
            vel.setX(-vel.x())
        ____ rightOverflow > 0.0:
            position.setX(position.x() - 2 * rightOverflow)
            vel.setX(-vel.x())

        __ topOverflow < 0.0:
            position.setY(position.y() - 2 * topOverflow)
            vel.setY(-vel.y())
        ____ bottomOverflow > 0.0:
            position.setY(position.y() - 2 * bottomOverflow)
            vel.setY(-vel.y())

    ___ rect 
        r_ QRectF(position.x() - radius,
                position.y() - radius, 2 * radius,
                2 * radius)


c_ GLWidget(QOpenGLWidget):
    ___  -   parent_None):
        s__(GLWidget, self). - (parent)

        midnight _ ?T..(0, 0, 0)
        random.seed(midnight.secsTo(?T...currentTime()))

        object _ 0
        xRot _ 0
        yRot _ 0
        zRot _ 0
        image _ QImage()
        bubbles _   # list
        lastPos _ QPoint()

        trolltechGreen _ ?C...fromCmykF(0.40, 0.0, 1.0, 0.0)
        trolltechPurple _ ?C...fromCmykF(0.39, 0.39, 0.0, 0.0)

        animationTimer _ ?T..
        animationTimer.setSingleShot F..
        animationTimer.timeout.c..(animate)
        animationTimer.start(25)

        setAutoFillBackground F..
        sMS..(200, 200)
        sWT..("Overpainting a Scene")

    ___ setXRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ xRot:
            xRot _ angle

    ___ setYRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ yRot:
            yRot _ angle

    ___ setZRotation  angle):
        angle _ normalizeAngle(angle)
        __ angle !_ zRot:
            zRot _ angle

    ___ initializeGL 
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        gl _ context().versionFunctions(version_profile)
        gl.initializeOpenGLFunctions()

        object _ makeObject()

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

    ___ paintEvent  event):
        makeCurrent()

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()

        setClearColor(trolltechPurple.darker())
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_DEPTH_TEST)
        #self.gl.glEnable(self.gl.GL_CULL_FACE)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glEnable(gl.GL_MULTISAMPLE)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION,
                (0.5, 5.0, 7.0, 1.0))

        setupViewport(width(), height())

        gl.glClear(
                gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -10.0)
        gl.glRotated(xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(zRot / 16.0, 0.0, 0.0, 1.0)
        gl.glCallList(object)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPopMatrix()

        painter _ QPainter
        painter.setRenderHint(QPainter.Antialiasing)

        ___ bubble __ bubbles:
            __ bubble.rect().intersects(QRectF(event.rect())):
                bubble.drawBubble(painter)

        drawInstructions(painter)
        painter.end()

    ___ resizeGL  width, height):
        setupViewport(width, height)

    ___ showEvent  event):
        createBubbles(20 - le.(bubbles))

    ___ sH..
        r_ ?S..(400, 400)

    ___ makeObject 
        li.. _ gl.glGenLists(1)
        gl.glNewList(li.., gl.GL_COMPILE)

        gl.glEnable(gl.GL_NORMALIZE)
        gl.glBegin(gl.GL_QUADS)

        gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE,
                (trolltechGreen.red()/255.0,
                 trolltechGreen.green()/255.0,
                 trolltechGreen.blue()/255.0, 1.0))

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
        r_ li..

    ___ quad  x1, y1, x2, y2, x3, y3, x4, y4):
        gl.glNormal3d(0.0, 0.0, -1.0)
        gl.glVertex3d(x1, y1, -0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x3, y3, -0.05)
        gl.glVertex3d(x4, y4, -0.05)

        gl.glNormal3d(0.0, 0.0, 1.0)
        gl.glVertex3d(x4, y4, +0.05)
        gl.glVertex3d(x3, y3, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x1, y1, +0.05)

    ___ extrude  x1, y1, x2, y2):
        sC..(trolltechGreen.darker(250 + in.(100 * x1)))

        gl.glNormal3d((x1 + x2)/2.0, (y1 + y2)/2.0, 0.0)
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

    ___ createBubbles  number):
        ___ i __ ra..(number):
            position _ QPointF(width()*(0.1 + 0.8*random.random()),
                               height()*(0.1 + 0.8*random.random()))
            radius _ min(width(), height())*(0.0125 + 0.0875*random.random())
            velocity _ QPointF(width()*0.0125*(-0.5 + random.random()),
                               height()*0.0125*(-0.5 + random.random()))

            bubbles.ap..(Bubble(position, radius, velocity))

    ___ animate 
        ___ bubble __ bubbles:
            bubble.move(rect())

        update()

    ___ setupViewport  width, height):
        side _ min(width, height)
        gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    ___ drawInstructions  painter):
        t__ _ "Click and drag with the left mouse button to rotate the Qt " \
                "logo."
        metrics _ QFontMetrics(font())
        border _ max(4, metrics.leading())

        rect _ metrics.boundingRect(0, 0, width() - 2*border,
                in.(height()*0.125), __.AlignCenter | __.TextWordWrap,
                t__)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.fillRect(QRect(0, 0, width(), rect.height() + 2*border),
                ?C..(0, 0, 0, 127))
        painter.sP..(__.white)
        painter.fillRect(QRect(0, 0, width(), rect.height() + 2*border),
                ?C..(0, 0, 0, 127))
        painter.drawText((width() - rect.width())/2, border, rect.width(),
                rect.height(), __.AlignCenter | __.TextWordWrap, t__)

    ___ setClearColor  c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    ___ sC..  c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


__ ______ __ ______

    app _ ?A..(___.a..

    fmt _ QSurfaceFormat()
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    window _ GLWidget()
    window.s..
    ___.e.. ?.e..
