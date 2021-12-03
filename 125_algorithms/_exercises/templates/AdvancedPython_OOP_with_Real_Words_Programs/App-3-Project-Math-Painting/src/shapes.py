c_ Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""
    ___  -    x, y, height, width, color):
        x = x
        y = y
        height = height
        width = width
        color = color

    ___ draw   canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[x: x + height, y: y + width] = color


c_ Square:
    """A square shape that can be drawn on a Canvas object"""
    ___  -    x, y, side, color):
        color = color
        x = x
        y = y
        side = side

    ___ draw   canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[x: x + side, y: y + side] = color