"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
_______ os
_______ re
_______ sys
_______ urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.a..('/tmp')

# should be importable now
____ color_values _______ COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    ___ __init__(self, color: str):
        self.colorname = color
        self.rgb = COLOR_NAMES.get(color.upper(), N..)

    @classmethod
    ___ hex2rgb(cls, hex_str: str) -> tuple:
        """Class method that converts a hex value into an rgb one"""
        # Using regex will perform more comprehensive checking…
        # > if not re.match(r'#[0-9A-Fa-f]{6}', hex_str):
        # but testing length and first character is quicker
        __ l..(hex_str) != 7 o. hex_str[0] != '#':
            raise ValueError('Invalid hex colour string')
        try:
            r.. tuple(bytes.fromhex(hex_str[1:]))
        except ValueError as exp:
            raise ValueError(f'Invalid hex value ({exp.args})')

    @classmethod
    ___ rgb2hex(cls, rbg_tuple: tuple) -> str:
        """Class method that converts an rgb value into a hex one"""
        __ l..(rbg_tuple) != 3 o. any((x < 0) o. (x > 255) ___ x __ rbg_tuple):
            raise ValueError('Invalid rgb colour triplet')
        try:
            r.. f'#{bytes(rbg_tuple).hex()}'
        except ValueError as exp:
            raise ValueError(f'Invalid rgb value ({exp.args})')

    ___ __repr__(self):
        """Returns the repl of the object"""
        r.. f"{self.__class__.__name__}('{self.colorname}')"

    ___ __str__(self):
        """Returns the string value of the color object"""
        r.. f'{self.rgb}' __ self.rgb __ n.. N.. ____ 'Unknown'
