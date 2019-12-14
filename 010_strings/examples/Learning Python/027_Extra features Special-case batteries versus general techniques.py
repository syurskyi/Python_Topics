print('{0:b}'.format((2 ** 16) - 1))  # Expression (only) binary format code
# print('%b' % ((2 ** 16) - 1))
print(bin((2 ** 16) - 1)) # But other more general options work too
print('%s' % bin((2 ** 16) - 1)) # Usable with both method and % expression
print('{}'.format(bin((2 ** 16) - 1))) # With 2.7/3.1+ relative numbering
print('%s' % bin((2 ** 16) - 1)[2:]) # Slice off 0b to get exact equivalent
print('{:,d}'.format(999999999999)) # New str.format method feature in 3.1/2.7
# print('%s' % commas(999999999999)) # But % is same with simple 8-line function
