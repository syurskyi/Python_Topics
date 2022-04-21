# ___ rgb_to_hex rgb
#     """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
#        boundaries (0, 255) and returns its converted hex, for example:
#        Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
#     __ 0 <_ ? 0 <_ 255 a.. 0 <_ ? 1 <_ 255 a.. 0 <_ ? 2 <_ 255
#         r.. #{0:02X}{1:02X}{2:02X} .f.. ?[0],? 1],? 2
#     ____
#         r.. V...
#
# #print(rgb_to_hex((0, 128, 192)))