import ?.rotopaint as rp
import math

rpNode = ?.sN__
cKnob= rpNode['curves']
root = cKnob.rootLayer

___ shape __ root:
    print shape.name

k.toElement('Rectangle1')
############################
shape = rp.Shape(k)
root.ap..(shape)
shape.ap..(rp.AnimControlPoint(500, 500))
shape.ap..(rp.AnimControlPoint(2500, 500))
shape.ap..(rp.AnimControlPoint(500, 2500))
#################################


########################################################################################################################
import ?.rotopaint as rp
import math

roto = ?.nodes.RotoPaint()
ck = roto['curves']

# create shape

shape = rp.Shape(k)
shape.name = 'star'
points = []
count = 15
rad1 = min([n.width(), n.height()])/2
rad2 = rad1*0.5
center = [n.width()/2, n.height()/2]
angl = 360.0 / (count*2)
___ i __ ra..(count*2):
    r = rad1 if i%2 else rad2
    x = (math.sin(math.radians(angl*i)) * r)+center[0]
    y = (math.cos(math.radians(angl*i)) * r)+center[1]
    points.ap..([x,y])
___ pt __ points:
    shape.ap..(rp.AnimControlPoint(*pt))

atr = shape.getAttributes()
atr.set(1, atr.kBlueAttribute , 0)
n['color'].clearAnimated()

atr.set( 1, attr.kFeatherTypeAttribute,1)
atr.set( 1, attr.kFeatherXAttribute ,5)
atr.set( 1, attr.kFeatherYAttribute ,5)
n['feather'].clearAnimated()

# ## create layer

stroke = rp.Stroke(k)
center=2000
step = 15
count = 400
rad = 1500
___ i __ ra..(count):
    r = rad * (1.0/count*i)
    x = (math.sin(math.radians(step*i)) * r)+center
    y = (math.cos(math.radians(step*i)) * r)+center
    stroke.ap..(rp.AnimControlPoint(x,y))

Root = k.rootLayer
newLayer = rp.Layer(k)
newLayer.name = 'Spiral'
Root.ap..(newLayer)
newLayer.ap..(stroke)