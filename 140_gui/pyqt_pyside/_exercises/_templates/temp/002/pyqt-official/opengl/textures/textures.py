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

____ ?.?C.. ______ pS.., QFileInfo, QPoint, ?S.., __, ?T..
____ ?.?G.. ______ (?C.., QImage, QMatrix4x4, QOpenGLShader,
        QOpenGLShaderProgram, QOpenGLTexture, QOpenGLVersionProfile,
        QSurfaceFormat)
____ ?.?W.. ______ ?A.., QGridLayout, QOpenGLWidget, ?W..


c_ GLWidget(QOpenGLWidget):

    c__ _ pS..()

    PROGRAM_VERTEX_ATTRIBUTE, PROGRAM_TEXCOORD_ATTRIBUTE _ ra..(2)

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

    ___  -   parent_None):
        s__(GLWidget, self). - (parent)

        clearColor _ ?C..(__.black)
        xRot _ 0
        yRot _ 0
        zRot _ 0
        program _ N..

        lastPos _ QPoint()

    ___ minimumSizeHint
        r_ ?S..(50, 50)

    ___ sH..
        r_ ?S..(200, 200)

    ___ rotateBy  xAngle, yAngle, zAngle):
        xRot +_ xAngle
        yRot +_ yAngle
        zRot +_ zAngle
        update()

    ___ setClearColor  color):
        clearColor _ color
        update()

    ___ initializeGL
        version_profile _ QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        gl _ context().versionFunctions(version_profile)
        gl.initializeOpenGLFunctions()

        makeObject()

        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)

        vshader _ QOpenGLShader(QOpenGLShader.Vertex, self)
        vshader.compileSourceCode(vsrc)

        fshader _ QOpenGLShader(QOpenGLShader.Fragment, self)
        fshader.compileSourceCode(fsrc)

        program _ QOpenGLShaderProgram()
        program.addShader(vshader)
        program.addShader(fshader)
        program.bindAttributeLocation('vertex',
                PROGRAM_VERTEX_ATTRIBUTE)
        program.bindAttributeLocation('texCoord',
                PROGRAM_TEXCOORD_ATTRIBUTE)
        program.link()

        program.bind()
        program.setUniformValue('texture', 0)

        program.enableAttributeArray(PROGRAM_VERTEX_ATTRIBUTE)
        program.enableAttributeArray(PROGRAM_TEXCOORD_ATTRIBUTE)
        program.setAttributeArray(PROGRAM_VERTEX_ATTRIBUTE,
                vertices)
        program.setAttributeArray(PROGRAM_TEXCOORD_ATTRIBUTE,
                texCoords)

    ___ paintGL
        gl.glClearColor(clearColor.redF(), clearColor.greenF(),
                clearColor.blueF(), clearColor.alphaF())
        gl.glClear(
                gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        m _ QMatrix4x4()
        m.ortho(-0.5, 0.5, 0.5, -0.5, 4.0, 15.0)
        m.translate(0.0, 0.0, -10.0)
        m.rotate(xRot / 16.0, 1.0, 0.0, 0.0)
        m.rotate(yRot / 16.0, 0.0, 1.0, 0.0)
        m.rotate(zRot / 16.0, 0.0, 0.0, 1.0)

        program.setUniformValue('matrix', m)

        ___ i, texture __ en..(textures):
            texture.bind()
            gl.glDrawArrays(gl.GL_TRIANGLE_FAN, i * 4, 4)

    ___ resizeGL  width, height):
        side _ min(width, height)
        gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

    ___ mousePressEvent  event):
        lastPos _ event.pos()

    ___ mouseMoveEvent  event):
        dx _ event.x() - lastPos.x()
        dy _ event.y() - lastPos.y()

        __ event.buttons() & __.LeftButton:
            rotateBy(8 * dy, 8 * dx, 0)
        ____ event.buttons() & __.RightButton:
            rotateBy(8 * dy, 0, 8 * dx)

        lastPos _ event.pos()

    ___ mouseReleaseEvent  event):
        c__.e..()

    ___ makeObject
        textures _   # list
        texCoords _   # list
        vertices _   # list

        root _ QFileInfo(__file__).absolutePath()

        ___ i __ ra..(6):
            textures.ap..(
                    QOpenGLTexture(
                            QImage(root + ('/images/side%d.png' % (i + 1))).mirrored()))

            ___ j __ ra..(4):
                texCoords.ap..(((j __ 0 or j __ 3), (j __ 0 or j __ 1)))

                x, y, z _ coords[i][j]
                vertices.ap..((0.2 * x, 0.2 * y, 0.2 * z))


c_ Window(?W..):
    NumRows _ 2
    NumColumns _ 3

    ___  -
        s__(Window, self). - ()

        glWidgets _   # list

        mainLayout _ QGridLayout()

        ___ i __ ra..(Window.NumRows):
            row _   # list

            ___ j __ ra..(Window.NumColumns):
                clearColor _ ?C..()
                clearColor.setHsv(((i * Window.NumColumns) + j) * 255
                                  / (Window.NumRows * Window.NumColumns - 1),
                                  255, 63)

                widget _ GLWidget()
                widget.setClearColor(clearColor)
                widget.rotateBy(+42 * 16, +42 * 16, -21 * 16)
                mainLayout.aW..(widget, i, j)

                widget.c__.c..(setCurrentGlWidget)

                row.ap..(widget)

            glWidgets.ap..(row)

        sL..(mainLayout)

        currentGlWidget _ glWidgets[0][0]

        timer _ ?T..
        timer.timeout.c..(rotateOneStep)
        timer.start(20)

        sWT..("Textures")

    ___ setCurrentGlWidget
        currentGlWidget _ sender()

    ___ rotateOneStep
        __ currentGlWidget:
            currentGlWidget.rotateBy(+2 * 16, +2 * 16, -1 * 16)


__ ______ __ ______

    app _ ?A..(___.a..

    f.. _ QSurfaceFormat()
    f...setDepthBufferSize(24)
    QSurfaceFormat.setDefaultFormat(f..)

    window _ Window()
    window.s..
    ___.e.. ?.e..
