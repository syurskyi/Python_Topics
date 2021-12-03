_____ numpy as np
____ PIL _____ Image


c_ Canvas:
    """Object where all shapes are going to be drawn"""

    ___  -    height, width, color):
        color = color
        height = height
        width = width

        # Create a 3d numpy array of zeros
        data = np.zeros((height, width, 3), dtype=np.uint8)
        # Change [0,0,0] with user given values for color
        data[:] = color

    ___ make   imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(data, 'RGB')
        img.save(imagepath)