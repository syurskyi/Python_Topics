"""Validate and specify triangle types"""

class TriangleError(Exception
    """Error if it cannot be a triangle"""
    ___ __init__(self, message
        super(TriangleError, self).__init__(message)

class Triangle(object
    """Validate and specify triangle types"""
    ___ __init__(self, a, b, c
        """Create and validate triangle"""
        (self.a, self.b, self.c) = sorted((a, b, c))
        __ self.a + self.b <= self.c:
            raise TriangleError("Not a Triangle")

    ___ kind(self
        """Specify triangle type"""
        __ self.a __ self.b and self.b __ self.c:
            r_ "equilateral"
        ____ self.a __ self.b or self.b __ self.c:
            r_ "isosceles"
        ____
            r_ "scalene"
