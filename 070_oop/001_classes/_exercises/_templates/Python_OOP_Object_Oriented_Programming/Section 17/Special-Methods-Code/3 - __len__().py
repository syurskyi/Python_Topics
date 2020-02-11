class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        """Distance from the origin (0,0) rounded to the nearest integer."""
        return round(self.x**2 + self.y**2)**(1/2))


