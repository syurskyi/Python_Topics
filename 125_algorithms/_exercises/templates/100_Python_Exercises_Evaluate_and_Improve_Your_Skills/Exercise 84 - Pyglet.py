#Please use the pyglet library to create a Hello world application

______ pyglet
window _ pyglet.window.Window()
label _ pyglet.text.Label('Hello, world',
                          font_name_'Times New Roman',
                          font_size_36,
                          x_window.width//2, y_window.height//2,
                          anchor_x_'center', anchor_y_'center')

@window.event
___ on_draw
    window.clear()
    label.draw()

pyglet.app.run()
