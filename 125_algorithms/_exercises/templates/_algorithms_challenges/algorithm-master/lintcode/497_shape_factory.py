"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    ___ draw(self):
        raise NotImplementedError('This method should have implemented.')


class Triangle(Shape):
    ___ draw(self):
        print '  /\\'
        print ' /  \\'
        print '/____\\'


class Rectangle(Shape):
    ___ draw(self):
        print ' ----'
        print '|    |'
        print ' ----'


class Square(Shape):
    ___ draw(self):
        print ' ----'
        print '|    |'
        print '|    |'
        print ' ----'


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    ___ getShape(self, shapeType):
        __ shapeType == 'Triangle':
            return Triangle()
        __ shapeType == 'Rectangle':
            return Rectangle()
        __ shapeType == 'Square':
            return Square()
