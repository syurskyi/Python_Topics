import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = COLOR_NAMES.get(color.upper())
        self.color = color

    def hex2rgb(hex_value):
        """Class method that converts a hex value into an rgb one"""
        if len(hex_value) != 7 or hex_value[0] != '#':
            raise ValueError
        try:
            rgb = tuple(int(hex_value.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        except ValueError:
            raise ValueError
        return rgb

    def rgb2hex(rgb_value):
        """Class method that converts an rgb value into a hex one"""
        for value in rgb_value:
            if int(value) < 0 or int(value) > 255:
                raise ValueError
        hex = '#%02x%02x%02x' % rgb_value
        return hex

    def __repr__(self):
        """Returns the repl of the object"""
        return "%s(%r)"%(self.__class__.__name__, self.color)

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else "Unknown"


#color = Color('orange')
#print(color.rgb2hex('(0, 128, 0)'))

#print(hex)