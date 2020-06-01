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

____ ?.QtCore ______ pyqtSignal, QFileInfo, QPoint, QSize, Qt, QTimer
____ ?.QtGui ______ (QColor, QImage, QMatrix4x4, QOpenGLShader,
        QOpenGLShaderProgram, QOpenGLTexture, QOpenGLVersionProfile,
        QSurfaceFormat)
____ ?.?W.. ______ ?A.., QGridLayout, QOpenGLWidget, QWidget


class GLWidget(QOpenGLWidget):

    c__ _ pyqtSignal()

    PROGRAM_VERTEX_ATTRIBUTE, PROGRAM_TEXCOORD_ATTRIBUTE _ range(2)

    vsrc _ """
attribute highp vec4 vertex;
attribute mediump vec4 texCoord;
varying mediump vec4 texc;
uniform mediump mat4 matrix;
void main(void)
{
    gl_Position = matrix * vertex;
    texc = texCoord;
}
"""

    fsrc _ """
uniform sampler2D texture;
varying mediump vec4 texc;
void main(void)
{
    gl_FragColor = texture2D(texture, texc.st);
}
"""

    coords _ (
        (( +1, -1, -1 ), ( -1, -1, -1 ), ( -1, +1, -1 ), ( +1, +1, -1 )),
        (( +1, +1, -1 ), ( -1, +1, -1 ), ( -1, +1, +1 ), ( +1, +1, +1 )),
        (( +1, -1, +1 ), ( +1, -1, -1 ), ( +1, +1, -1 ), ( +1, +1, +1 )),
        (( -1, -1, -1 ), ( -1, -1, +1 ), ( -1, +1, +1 ), ( -1, +1, -1 )),
        (( +1, -1, +1 ), ( -1, -1, +1 ), ( -1, -1, -1 ), ( +1, -1, -1 )),
        (( -1, -1, +1 ), ( +1, -1, +1 ), ( +1, +1, +1 ), ( -1, +1, +1 ))
    )

    ___ __init__(self, parent_None):
        super(GLWidget, self).__init__(parent)

        self.clearColor _ QColor(Qt.black)
        self.xRot _ 0
        self.yRot _ 0
        self.zRot _ 0
        self.program _ None

        self.lastPos _ QPoint()

    ___ minimumSizeHint(self):
        return QSize(50, 50)

    ___ sizeHint(self):
        return QSize(200, 200)

    ___ rotateBy(self, xAngle, yAngle, zAngle):
        self.xRot +_ xAngle
        self.yRot +_ yAngle
        self.zRot +_ zAngle
        self.update()

    ___ setClearColor(self, color):
        self.clearColor _ color
        self.update()

    ___ initializeGL(self):
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl _ self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()

        self.makeObject()

        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_CULL_FACE)

        vshader _ QOpenGLShader(QOpenGLShader.Vertex, self)
        vshader.compileSourceCode(self.vsrc)

        fshader _ QOpenGLShader(QOpenGLShader.Fragment, self)
        fshader.compileSourceCode(self.fsrc)

        self.program _ QOpenGLShaderProgram()
        self.program.addShader(vshader)
        self.program.addShader(fshader)
        self.program.bindAttributeLocation('vertex',
                self.PROGRAM_VERTEX_ATTRIBUTE)
        self.program.bindAttributeLocation('texCoord',
                self.PROGRAM_TEXCOORD_ATTRIBUTE)
        self.program.link()

        self.program.bind()
        self.program.setUniformValue('texture', 0)

        self.program.enableAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE)
        self.program.enableAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE)
        self.program.setAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE,
                self.vertices)
        self.program.setAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE,
                self.texCoords)

    ___ paintGL(self):
        self.gl.glClearColor(self.clearColor.redF(), self.clearColor.greenF(),
                self.clearColor.blueF(), self.clearColor.alphaF())
        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)

        m _ QMatrix4x4()
        m.ortho(-0.5, 0.5, 0.5, -0.5, 4.0, 15.0)
        m.translate(0.0, 0.0, -10.0)
        m.rotate(self.xRot / 16.0, 1.0, 0.0, 0.0)
        m.rotate(self.yRot / 16.0, 0.0, 1.0, 0.0)
        m.rotate(self.zRot / 16.0, 0.0, 0.0, 1.0)

        self.program.setUniformValue('matrix', m)

        for i, texture in enumerate(self.textures):
            texture.bind()
            self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, i * 4, 4)

    ___ resizeGL(self, width, height):
        side _ min(width, height)
        self.gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

    ___ mousePressEvent(self, event):
        self.lastPos _ event.pos()

    ___ mouseMoveEvent(self, event):
        dx _ event.x() - self.lastPos.x()
        dy _ event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.rotateBy(8 * dy, 8 * dx, 0)
        elif event.buttons() & Qt.RightButton:
            self.rotateBy(8 * dy, 0, 8 * dx)

        self.lastPos _ event.pos()

    ___ mouseReleaseEvent(self, event):
        self.c__.emit()

    ___ makeObject(self):
        self.textures _ []
        self.texCoords _ []
        self.vertices _ []

        root _ QFileInfo(__file__).absolutePath()

        for i in range(6):
            self.textures.append(
                    QOpenGLTexture(
                            QImage(root + ('/images/side%d.png' % (i + 1))).mirrored()))

            for j in range(4):
                self.texCoords.append(((j == 0 or j == 3), (j == 0 or j == 1)))

                x, y, z _ self.coords[i][j]
                self.vertices.append((0.2 * x, 0.2 * y, 0.2 * z))


class Window(QWidget):
    NumRows _ 2
    NumColumns _ 3

    ___ __init__(self):
        super(Window, self).__init__()

        self.glWidgets _ []

        mainLayout _ QGridLayout()

        for i in range(Window.NumRows):
            row _ []

            for j in range(Window.NumColumns):
                clearColor _ QColor()
                clearColor.setHsv(((i * Window.NumColumns) + j) * 255
                                  / (Window.NumRows * Window.NumColumns - 1),
                                  255, 63)

                widget _ GLWidget()
                widget.setClearColor(clearColor)
                widget.rotateBy(+42 * 16, +42 * 16, -21 * 16)
                mainLayout.addWidget(widget, i, j)

                widget.c__.c..(self.setCurrentGlWidget)

                row.append(widget)

            self.glWidgets.append(row)

        self.setLayout(mainLayout)

        self.currentGlWidget _ self.glWidgets[0][0]

        timer _ QTimer(self)
        timer.timeout.c..(self.rotateOneStep)
        timer.start(20)

        self.setWindowTitle("Textures")

    ___ setCurrentGlWidget(self):
        self.currentGlWidget _ self.sender()

    ___ rotateOneStep(self):
        if self.currentGlWidget:
            self.currentGlWidget.rotateBy(+2 * 16, +2 * 16, -1 * 16)


if __name__ == '__main__':

    app _ ?A..(sys.argv)

    format _ QSurfaceFormat()
    format.setDepthBufferSize(24)
    QSurfaceFormat.setDefaultFormat(format)

    window _ Window()
    window.s..
    sys.exit(app.exec_())
