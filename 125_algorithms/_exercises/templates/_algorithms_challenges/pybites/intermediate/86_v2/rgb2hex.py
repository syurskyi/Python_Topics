___ rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""


    __ any(n.. 0 <= value <= 255 ___ value __ rgb):
        raise ValueError("Not in range")


    
    hex_value = ''.j..(hex(value)[2:].zfill(2) ___ value __ rgb).upper()


    r.. f"#{hex_value}"









