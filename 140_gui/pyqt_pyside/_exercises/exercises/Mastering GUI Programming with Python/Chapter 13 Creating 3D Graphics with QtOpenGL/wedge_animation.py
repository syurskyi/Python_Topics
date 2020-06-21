____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
______ ___


c_ MainWindow(qtw.?MW..):

    ___  -  
        s_. - ()

        # Your code goes here
        r..(800, 600)
        main _ qtw.?W..
        sCW..(main)
        main.sL.. ?.?VBL..
        oglw _ GlWidget()
        main.la__ .aW..(oglw)

        # Animation controls
        btn_layout _ ?.?HBL..
        main.la__ .aL..(btn_layout)
        ___ direction __ ('none', 'left', 'right', 'up', 'down'):
            button _ qtw.?PB..(
                direction,
                autoExclusive_True,
                checkable_True,
                c___getattr(oglw, f'spin_{direction}')
                )
            btn_layout.aW..(button)
        zoom_layout _ ?.?HBL..
        main.la__ .aL..(zoom_layout)
        zoom_in _ qtw.?PB..('zoom in', c___oglw.zoom_in)
        zoom_layout.aW..(zoom_in)
        zoom_out _ qtw.?PB..('zoom out', c___oglw.zoom_out)
        zoom_layout.aW..(zoom_out)
        s..


c_ GlWidget(qtw.QOpenGLWidget):
    """A widget to display our OpenGL drawing"""

    ___ initializeGL 
        s_.initializeGL()

        # Fetch version-specific functions
        gl_context _ context()
        version _ qtg.QOpenGLVersionProfile()
        version.setVersion(2, 1)
        gl _ gl_context.versionFunctions(version)

        # Configure
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glDepthFunc(gl.GL_LESS)
        gl.glEnable(gl.GL_CULL_FACE)

        # Create the program
        program _ qtg.QOpenGLShaderProgram()
        program.addShaderFromSourceFile(
            qtg.QOpenGLShader.Vertex, 'vertex_shader.glsl')
        program.addShaderFromSourceFile(
            qtg.QOpenGLShader.Fragment, 'fragment_shader.glsl')
        program.link()

        # Get variable locations
        vertex_location _ program.attributeLocation('vertex')
        matrix_location _ program.uniformLocation('matrix')
        color_location _ program.attributeLocation('color_attr')

        # Create transformation matrix
        view_matrix _ qtg.QMatrix4x4()
        view_matrix.perspective(
            45,  # Angle
            width() / height(),  # Aspect Ratio
            0.1,  # Near clipping plane
            100.0  # Far clipping plane
        )
        view_matrix.translate(0, 0, -5)
        rotation _ [0, 0, 0, 0]

    ___ paintGL 
        # Fill the window with dark violet
        gl.glClearColor(0.1, 0, 0.2, 1)
        gl.glClear(
            gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        program.bind()

        # Drawing
        front_vertices _ [
            qtg.QVector3D(0.0, 1.0, 0.0),  # Peak
            qtg.QVector3D(-1.0, 0.0, 0.0),  # Bottom left
            qtg.QVector3D(1.0, 0.0, 0.0)  # Bottom right
            ]

        face_colors _ (
            qtg.?C..('red'),
            qtg.?C..('orange'),
            qtg.?C..('yellow'),
        )
        gl_colors _ [
            qcolor_to_glvec(color)
            ___ color __ face_colors
        ]
        program.setUniformValue(
            matrix_location, view_matrix)
        program.enableAttributeArray(vertex_location)
        program.setAttributeArray(vertex_location, front_vertices)
        program.enableAttributeArray(color_location)
        program.setAttributeArray(color_location, gl_colors)

        # Draw the front
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
        # Draw the back
        back_vertices _ [
            qtg.QVector3D(x.toVector2D(), -0.5)
            ___ x __ front_vertices]
        program.setAttributeArray(
            vertex_location, reversed(back_vertices))
            # If you try the line below instead, the back side
            # will not show unless you disable face culling
            #self.vertex_location, back_vertices)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

        # draw the sides
        sides _ [(0, 1), (1, 2), (2, 0)]
        side_vertices _ li..()
        ___ index1, index2 __ sides:
            side_vertices +_ [
                front_vertices[index1],
                back_vertices[index1],
                back_vertices[index2],
                front_vertices[index2]
            ]
        side_colors _ [
            qtg.?C..('blue'),
            qtg.?C..('purple'),
            qtg.?C..('cyan'),
            qtg.?C..('magenta'),
        ]
        gl_colors _ [
            qcolor_to_glvec(color)
            ___ color __ side_colors
        ] * 3

        program.setAttributeArray(color_location, gl_colors)
        program.setAttributeArray(vertex_location, side_vertices)
        gl.glDrawArrays(gl.GL_QUADS, 0, le.(side_vertices))
        program.disableAttributeArray(vertex_location)
        program.disableAttributeArray(color_location)
        program.release()

        # Animation
        # rotate
        view_matrix.rotate(*rotation)
        update()

    ___ qcolor_to_glvec  qcolor):
        r_ qtg.QVector3D(
            qcolor.red() / 255,
            qcolor.green() / 255,
            qcolor.blue() / 255
        )

    ___ spin_none 
        rotation _ [0, 0, 0, 0]

    ___ spin_left 
        rotation _ [-1, 0, 1, 0]

    ___ spin_right 
        rotation _ [1, 0, 1, 0]

    ___ spin_up 
        rotation _ [1, 1, 0, 0]

    ___ spin_down 
        rotation _ [-1, 1, 0, 0]

    ___ zoom_in 
        view_matrix.scale(1.1, 1.1, 1.1)

    ___ zoom_out 
        view_matrix.scale(.9, .9, .9)


__ ______ __ ______
    app _ qtw.?A..(___.a..
    mw _ MainWindow()
    app.e..
