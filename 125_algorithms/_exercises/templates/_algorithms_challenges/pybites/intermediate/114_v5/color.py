"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
_______ __
_______ __
_______ ___
_______ u__.r..

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module __.p...j..('/tmp', 'color_values.py')
u__.r...u..('https://bit.ly/2MSuu4z',
                           color_values_module)
___.p...a..('/tmp')

# should be importable now
____ color_values _______ COLOR_NAMES  # noqa E402


c_ Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    ___ - , color: s..
        colorname color
        rgb COLOR_NAMES.g.. color.u.., N..)

    @classmethod
    ___ hex2rgb(cls, hex_str: s..) __ t..:
        """Class method that converts a hex value into an rgb one"""
        # Using regex will perform more comprehensive checking…
        # > if not re.match(r'#[0-9A-Fa-f]{6}', hex_str):
        # but testing length and first character is quicker
        __ l..(hex_str) !_ 7 o. hex_str[0] !_ '#':
            r.. V...('Invalid hex colour string')
        ___
            r.. t..(bytes.fromhex(hex_str[1:]
        ______ V... __ exp:
            r.. V... _*Invalid hex value ({exp.args})')

    @classmethod
    ___ rgb2hex(cls, rbg_tuple: t..) __ s..
        """Class method that converts an rgb value into a hex one"""
        __ l..(rbg_tuple) !_ 3 o. a__((x < 0) o. (x > 255) ___ x __ rbg_tuple
            r.. V...('Invalid rgb colour triplet')
        ___
            r.. f'#{bytes(rbg_tuple).hex()}'
        ______ V... __ exp:
            r.. V... _*Invalid rgb value ({exp.args})')

    ___  -r
        """Returns the repl of the object"""
        r.. f"{__class__.__name__}('{colorname}')"

    ___ -s
        """Returns the string value of the color object"""
        r.. _* rgb}' __ rgb __ n.. N.. ____ 'Unknown'
