_____ ?

# int('%02x%02x%02x%02x' % (255,0,0,255),16)

___ hexColor(r,g,b, double=True):
    m = 255
    __ no. double:
        m = 1
    r_ int('%02x%02x%02x%02x' % (r*m,g*m,b*m,1*m),16)

tr = ?.createNode('Transform')
tr['tile_color'].setValue(hexColor(1,0,1))

color = ?.getColor()