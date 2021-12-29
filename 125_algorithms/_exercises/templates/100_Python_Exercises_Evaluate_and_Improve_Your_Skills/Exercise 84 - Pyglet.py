#Please use the pyglet library to create a Hello world application

import pyglet
window  pyglet.window.Window()
label  pyglet.text.Label('Hello, world',
                          font_name'Times New Roman',
                          font_size36,
                          xwindow.width//2, ywindow.height//2,
                          anchor_x'center', anchor_y'center')

@window.event
___ on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
