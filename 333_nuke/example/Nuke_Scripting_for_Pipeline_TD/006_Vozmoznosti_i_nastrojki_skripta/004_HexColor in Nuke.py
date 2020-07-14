import nuke

# int('%02x%02x%02x%02x' % (255,0,0,255),16)

def hexColor(r,g,b, double=True):
    m = 255
    if not double:
        m = 1
    return int('%02x%02x%02x%02x' % (r*m,g*m,b*m,1*m),16)

tr = nuke.createNode('Transform')
tr['tile_color'].setValue(hexColor(1,0,1))

color = nuke.getColor()