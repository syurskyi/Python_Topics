class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x <= other.x

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y)

    def __gt__(self, other):
        return self.x > other.x

    def __ge__(self, other):
        return self.x >= other.x

