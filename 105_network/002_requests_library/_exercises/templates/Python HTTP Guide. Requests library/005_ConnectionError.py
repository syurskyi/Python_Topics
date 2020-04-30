______ r__
try:
    response = ?.g..('http://urldoesnotexistforsure.bom')
except ?.exceptions.ConnectionError:
    print('Seems like dns lookup failed..')

# Seems like dns lookup failed..