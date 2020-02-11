class Rectangle:

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

class GUIElement:

    def click():
        print("The object was clicked...")

class Button(Rectangle, GUIElement):

    def __init__(self, length, width, color, text):
        Rectangle.__init__(self, length, width, color)
        self.text = text
