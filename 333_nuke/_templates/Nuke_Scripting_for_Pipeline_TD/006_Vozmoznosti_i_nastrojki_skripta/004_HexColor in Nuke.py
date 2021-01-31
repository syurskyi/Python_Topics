_____ ?

# int('%02x%02x%02x%02x' % (255,0,0,255),16)

___ hexColor(r,g,b, double=T..):
    m = 255
    __ no. double:
        m = 1
    r_ in_('%02x%02x%02x%02x' % (r*m,g*m,b*m,1*m),16)

tr = ?.cN..('Transform')
tr['tile_color'].sV..(hexColor(1,0,1))

color = ?.getColor()