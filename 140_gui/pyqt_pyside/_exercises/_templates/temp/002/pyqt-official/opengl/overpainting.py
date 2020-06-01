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
______ math, random

____ ?.QtCore ______ (QPoint, QPointF, QRect, QRectF, QSize, Qt, QTime,
        QTimer)
____ ?.QtGui ______ (QBrush, QColor, QFontMetrics, QImage,
        QOpenGLVersionProfile, QPainter, QRadialGradient, QSurfaceFormat)
____ ?.?W.. ______ QApplication, QOpenGLWidget


class Bubble(object):
    ___ __init__(self, position, radius, velocity):
        self.position _ position
        self.vel _ velocity
        self.radius _ radius

        self.innerColor _ self.randomColor()
        self.outerColor _ self.randomColor()
        self.updateBrush()

    ___ updateBrush(self):
        gradient _ QRadialGradient(QPointF(self.radius, self.radius),
                self.radius, QPointF(self.radius*0.5, self.radius*0.5))

        gradient.setColorAt(0, QColor(255, 255, 255, 255))
        gradient.setColorAt(0.25, self.innerColor)
        gradient.setColorAt(1, self.outerColor)
        self.brush _ QBrush(gradient)

    ___ drawBubble(self, painter):
        painter.save()
        painter.translate(self.position.x() - self.radius,
                self.position.y() - self.radius)
        painter.setBrush(self.brush)
        painter.drawEllipse(0, 0, int(2*self.radius), int(2*self.radius))
        painter.restore()

    ___ randomColor(self):
        red _ random.randrange(205, 256)
        green _ random.randrange(205, 256)
        blue _ random.randrange(205, 256)
        alpha _ random.randrange(91, 192)

        return QColor(red, green, blue, alpha)

    ___ move(self, bbox):
        self.position +_ self.vel
        leftOverflow _ self.position.x() - self.radius - bbox.left()
        rightOverflow _ self.position.x() + self.radius - bbox.right()
        topOverflow _ self.position.y() - self.radius - bbox.top()
        bottomOverflow _ self.position.y() + self.radius - bbox.bottom()

        if leftOverflow < 0.0:
            self.position.setX(self.position.x() - 2 * leftOverflow)
            self.vel.setX(-self.vel.x())
        elif rightOverflow > 0.0:
            self.position.setX(self.position.x() - 2 * rightOverflow)
            self.vel.setX(-self.vel.x())

        if topOverflow < 0.0:
            self.position.setY(self.position.y() - 2 * topOverflow)
            self.vel.setY(-self.vel.y())
        elif bottomOverflow > 0.0:
            self.position.setY(self.position.y() - 2 * bottomOverflow)
            self.vel.setY(-self.vel.y())

    ___ rect(self):
        return QRectF(self.position.x() - self.radius,
                self.position.y() - self.radius, 2 * self.radius,
                2 * self.radius)


class GLWidget(QOpenGLWidget):
    ___ __init__(self, parent_None):
        super(GLWidget, self).__init__(parent)

        midnight _ QTime(0, 0, 0)
        random.seed(midnight.secsTo(QTime.currentTime()))

        self.object _ 0
        self.xRot _ 0
        self.yRot _ 0
        self.zRot _ 0
        self.image _ QImage()
        self.bubbles _ []
        self.lastPos _ QPoint()

        self.trolltechGreen _ QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple _ QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

        self.animationTimer _ QTimer()
        self.animationTimer.setSingleShot(False)
        self.animationTimer.timeout.c..(self.animate)
        self.animationTimer.start(25)

        self.setAutoFillBackground(False)
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Overpainting a Scene")

    ___ setXRotation(self, angle):
        angle _ self.normalizeAngle(angle)
        if angle !_ self.xRot:
            self.xRot _ angle

    ___ setYRotation(self, angle):
        angle _ self.normalizeAngle(angle)
        if angle !_ self.yRot:
            self.yRot _ angle

    ___ setZRotation(self, angle):
        angle _ self.normalizeAngle(angle)
        if angle !_ self.zRot:
            self.zRot _ angle

    ___ initializeGL(self):
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl _ self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()

        self.object _ self.makeObject()

    ___ mousePressEvent(self, event):
        self.lastPos _ event.pos()

    ___ mouseMoveEvent(self, event):
        dx _ event.x() - self.lastPos.x()
        dy _ event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos _ event.pos()

    ___ paintEvent(self, event):
        self.makeCurrent()

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPushMatrix()

        self.setClearColor(self.trolltechPurple.darker())
        self.gl.glShadeModel(self.gl.GL_SMOOTH)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        #self.gl.glEnable(self.gl.GL_CULL_FACE)
        self.gl.glEnable(self.gl.GL_LIGHTING)
        self.gl.glEnable(self.gl.GL_LIGHT0)
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)
        self.gl.glLightfv(self.gl.GL_LIGHT0, self.gl.GL_POSITION,
                (0.5, 5.0, 7.0, 1.0))

        self.setupViewport(self.width(), self.height())

        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(0.0, 0.0, -10.0)
        self.gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        self.gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        self.gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        self.gl.glCallList(self.object)

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPopMatrix()

        painter _ QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for bubble in self.bubbles:
            if bubble.rect().intersects(QRectF(event.rect())):
                bubble.drawBubble(painter)

        self.drawInstructions(painter)
        painter.end()

    ___ resizeGL(self, width, height):
        self.setupViewport(width, height)

    ___ showEvent(self, event):
        self.createBubbles(20 - len(self.bubbles))

    ___ sizeHint(self):
        return QSize(400, 400)

    ___ makeObject(self):
        list _ self.gl.glGenLists(1)
        self.gl.glNewList(list, self.gl.GL_COMPILE)

        self.gl.glEnable(self.gl.GL_NORMALIZE)
        self.gl.glBegin(self.gl.GL_QUADS)

        self.gl.glMaterialfv(self.gl.GL_FRONT, self.gl.GL_DIFFUSE,
                (self.trolltechGreen.red()/255.0,
                 self.trolltechGreen.green()/255.0,
                 self.trolltechGreen.blue()/255.0, 1.0))

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
        return list

    ___ quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.gl.glNormal3d(0.0, 0.0, -1.0)
        self.gl.glVertex3d(x1, y1, -0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x3, y3, -0.05)
        self.gl.glVertex3d(x4, y4, -0.05)

        self.gl.glNormal3d(0.0, 0.0, 1.0)
        self.gl.glVertex3d(x4, y4, +0.05)
        self.gl.glVertex3d(x3, y3, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x1, y1, +0.05)

    ___ extrude(self, x1, y1, x2, y2):
        self.setColor(self.trolltechGreen.darker(250 + int(100 * x1)))

        self.gl.glNormal3d((x1 + x2)/2.0, (y1 + y2)/2.0, 0.0)
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

    ___ createBubbles(self, number):
        for i in range(number):
            position _ QPointF(self.width()*(0.1 + 0.8*random.random()),
                               self.height()*(0.1 + 0.8*random.random()))
            radius _ min(self.width(), self.height())*(0.0125 + 0.0875*random.random())
            velocity _ QPointF(self.width()*0.0125*(-0.5 + random.random()),
                               self.height()*0.0125*(-0.5 + random.random()))

            self.bubbles.append(Bubble(position, radius, velocity))

    ___ animate(self):
        for bubble in self.bubbles:
            bubble.move(self.rect())

        self.update()

    ___ setupViewport(self, width, height):
        side _ min(width, height)
        self.gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    ___ drawInstructions(self, painter):
        text _ "Click and drag with the left mouse button to rotate the Qt " \
                "logo."
        metrics _ QFontMetrics(self.font())
        border _ max(4, metrics.leading())

        rect _ metrics.boundingRect(0, 0, self.width() - 2*border,
                int(self.height()*0.125), Qt.AlignCenter | Qt.TextWordWrap,
                text)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.fillRect(QRect(0, 0, self.width(), rect.height() + 2*border),
                QColor(0, 0, 0, 127))
        painter.setPen(Qt.white)
        painter.fillRect(QRect(0, 0, self.width(), rect.height() + 2*border),
                QColor(0, 0, 0, 127))
        painter.drawText((self.width() - rect.width())/2, border, rect.width(),
                rect.height(), Qt.AlignCenter | Qt.TextWordWrap, text)

    ___ setClearColor(self, c):
        self.gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    ___ setColor(self, c):
        self.gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


if __name__ == '__main__':

    app _ QApplication(sys.argv)

    fmt _ QSurfaceFormat()
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    window _ GLWidget()
    window.s..
    sys.exit(app.exec_())
