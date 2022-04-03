import os
import sys
import u__.r..

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402
print(COLOR_NAMES)

class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper())

    @staticmethod
    def hex2rgb(hex_value):
        """Class method that converts a hex value into an rgb one"""
        if type(hex_value) != str or len(hex_value) != 7:
            raise ValueError("Hex value must be length 6 string starting with #")
        


        values = []

        for i in range(1,len(hex_value),2):
            h = hex_value[i:i + 2]
            try:
                value = int(h,16)
            except:
                raise 
            else:
                values.append(value)


        return tuple(values)















    @staticmethod
    def rgb2hex(rgb_value):
        """Class method that converts an rgb value into a hex one"""
        if type(rgb_value) not in [list,tuple] or len(rgb_value) != 3:
            raise ValueError("rgb value must be list or tuple of length 3")
        

        values = []
        for value in rgb_value:
            if not 0 <= value <= 255:
                raise ValueError("Invalid value")

            hex_value = f"{hex(value):0<2}"
            hex_value = hex_value[2:]
            if hex_value == '0':
                hex_value = hex_value.zfill(2)
            values.append(hex_value)
        
        return '#' + ''.join(values)







            





    def __repr__(self):
        """Returns the repl of the object"""
        return f"{type(self).__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""

        if self.rgb:
            return str(self.rgb)
        else:
            return "Unknown"


