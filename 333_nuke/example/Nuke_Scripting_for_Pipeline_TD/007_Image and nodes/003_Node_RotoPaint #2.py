import nuke.rotopaint as rp
import math

rpNode = nuke.selectedNode()
cKnob= rpNode['curves']
root = cKnob.rootLayer

for shape in root:
    print shape.name

k.toElement('Rectangle1')
############################
shape = rp.Shape(k)
root.append(shape)
shape.append(rp.AnimControlPoint(500, 500))
shape.append(rp.AnimControlPoint(2500, 500))
shape.append(rp.AnimControlPoint(500, 2500))
#################################


########################################################################################################################
import nuke.rotopaint as rp
import math

roto = nuke.nodes.RotoPaint()
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
for i in range(count*2):
    r = rad1 if i%2 else rad2
    x = (math.sin(math.radians(angl*i)) * r)+center[0]
    y = (math.cos(math.radians(angl*i)) * r)+center[1]
    points.append([x,y])
for pt in points:
    shape.append(rp.AnimControlPoint(*pt))

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
for i in range(count):
    r = rad * (1.0/count*i)
    x = (math.sin(math.radians(step*i)) * r)+center
    y = (math.cos(math.radians(step*i)) * r)+center
    stroke.append(rp.AnimControlPoint(x,y))

Root = k.rootLayer
newLayer = rp.Layer(k)
newLayer.name = 'Spiral'
Root.append(newLayer)
newLayer.append(stroke)