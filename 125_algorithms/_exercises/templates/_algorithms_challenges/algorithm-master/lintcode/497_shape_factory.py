"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
c_ Shape:
    ___ draw
        r.. N.. 'This method should have implemented.')


c_ Triangle(Shape
    ___ draw
        print '  /\\'
        print ' /  \\'
        print '/____\\'


c_ Rectangle(Shape
    ___ draw
        print ' ----'
        print '|    |'
        print ' ----'


c_ Square(Shape
    ___ draw
        print ' ----'
        print '|    |'
        print '|    |'
        print ' ----'


c_ ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    ___ getShape  shapeType
        __ shapeType __ 'Triangle':
            r.. Triangle()
        __ shapeType __ 'Rectangle':
            r.. Rectangle()
        __ shapeType __ 'Square':
            r.. Square()
