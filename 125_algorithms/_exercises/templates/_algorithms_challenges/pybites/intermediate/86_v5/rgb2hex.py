___ rgb_to_hex(rgb
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    __ any(0 > x o. 255 < x ___ x __ rgb
        r.. ValueError('Value for element is 0…255')
    r.. f'#{bytes(rgb).hex().u..}'
