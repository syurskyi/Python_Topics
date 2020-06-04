#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
## Contact: http://www.qt-project.org/legal
##
## This file is part of the documentation of the Qt Toolkit.
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
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
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


______ array

____ ?.?C.. ______ QEvent
____ ?.?G.. ______ (QGuiApplication, QMatrix4x4, QOpenGLContext,
        QOpenGLShader, QOpenGLShaderProgram, QOpenGLVersionProfile,
        QSurfaceFormat, QWindow)


c_ OpenGLWindow(QWindow):
    ___  -   parent_None):
        s__(OpenGLWindow, self). - (parent)

        m_update_pending _ F..
        m_animating _ F..
        m_context _ N..
        m_gl _ N..

        setSurfaceType(QWindow.OpenGLSurface)

    ___ initialize 
        p..

    ___ setAnimating  animating):
        m_animating _ animating

        __ animating:
            renderLater()

    ___ renderLater 
        __ no. m_update_pending:
            m_update_pending _ T..
            QGuiApplication.postEvent  QEvent(QEvent.UpdateRequest))

    ___ renderNow 
        __ no. isExposed
            r_

        m_update_pending _ F..

        needsInitialize _ F..

        __ m_context __ N..:
            m_context _ QOpenGLContext
            m_context.setFormat(requestedFormat())
            m_context.create()

            needsInitialize _ T..

        m_context.makeCurrent

        __ needsInitialize:
            version_profile _ QOpenGLVersionProfile()
            version_profile.setVersion(2, 0)
            m_gl _ m_context.versionFunctions(version_profile)
            m_gl.initializeOpenGLFunctions()

            initialize()

        render(m_gl)

        m_context.swapBuffers

        __ m_animating:
            renderLater()

    ___ event  event):
        __ event.type() __ QEvent.UpdateRequest:
            renderNow()
            r_ T..

        r_ s__(OpenGLWindow, self).event(event)

    ___ exposeEvent  event):
        renderNow()

    ___ resizeEvent  event):
        renderNow()


c_ TriangleWindow(OpenGLWindow):
    vertexShaderSource _ '''
attribute highp vec4 posAttr;
attribute lowp vec4 colAttr;
varying lowp vec4 col;
uniform highp mat4 matrix;
void main() {
    col = colAttr;
    gl_Position = matrix * posAttr;
}
'''

    fragmentShaderSource _ '''
varying lowp vec4 col;
void main() {
    gl_FragColor = col;
}
'''

    ___  -
        s__(TriangleWindow, self). - ()

        m_program _ 0
        m_frame _ 0

        m_posAttr _ 0
        m_colAttr _ 0
        m_matrixUniform _ 0

    ___ initialize 
        m_program _ QOpenGLShaderProgram

        m_program.addShaderFromSourceCode(QOpenGLShader.Vertex,
                vertexShaderSource)
        m_program.addShaderFromSourceCode(QOpenGLShader.Fragment,
                fragmentShaderSource)

        m_program.link()

        m_posAttr _ m_program.attributeLocation('posAttr')
        m_colAttr _ m_program.attributeLocation('colAttr')
        m_matrixUniform _ m_program.uniformLocation('matrix')

    ___ render  gl):
        gl.glViewport(0, 0, width(), height())

        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        m_program.bind()

        matrix _ QMatrix4x4()
        matrix.perspective(60, 4.0/3.0, 0.1, 100.0)
        matrix.translate(0, 0, -2)
        matrix.rotate(100.0 * m_frame / screen().refreshRate(),
                0, 1, 0)

        m_program.setUniformValue(m_matrixUniform, matrix)

        vertices _ array.array('f', [
                 0.0,  0.707,
                -0.5, -0.5,
                 0.5, -0.5])

        gl.glVertexAttribPointer(m_posAttr, 2, gl.GL_FLOAT, F.., 0,
                vertices)
        gl.glEnableVertexAttribArray(m_posAttr)

        colors _ array.array('f', [
                1.0, 0.0, 0.0,
                0.0, 1.0, 0.0,
                0.0, 0.0, 1.0])

        gl.glVertexAttribPointer(m_colAttr, 3, gl.GL_FLOAT, F.., 0,
                colors)
        gl.glEnableVertexAttribArray(m_colAttr)

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

        m_program.release()

        m_frame +_ 1


__ ______ __ ______

    ______ ___

    app _ QGuiApplication(___.a..

    f.. _ QSurfaceFormat()
    f...setSamples(4)

    window _ TriangleWindow()
    window.setFormat(f..)
    window.r..(640, 480)
    window.s..

    window.setAnimating( st.

    ___.e.. ?.e..
