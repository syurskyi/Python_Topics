class Triangle:

    # Body
    
    def find_area(self, base, height):
        """Return the area of a triangle.

        Find the area of a triangle using the base
        and the height provided. These values must be
        positive or zero.

        Args:
            base: A positive integer that represents the length
                of the base of the triangle. This value can be zero.
            height: A positive integer that represents the length
                of the height of the triangle. This value can be zero.

        Returns:
            A float that represents the area of the triangle.

        Raises:
            ValueError: the base or the height or both are not valid.

        """

        if base < 0 or height < 0:
            raise ValueError("The base and height must be either positive or zero")
        
        return (base * height)/2

    
