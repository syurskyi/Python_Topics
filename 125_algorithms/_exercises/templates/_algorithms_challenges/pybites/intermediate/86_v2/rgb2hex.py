___ rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""


    __ any(not 0 <= value <= 255 for value in rgb):
        raise ValueError("Not in range")


    
    hex_value = ''.join(hex(value)[2:].zfill(2) for value in rgb).upper()


    return f"#{hex_value}"









