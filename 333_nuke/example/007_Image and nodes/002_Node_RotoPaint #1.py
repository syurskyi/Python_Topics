import nuke.rotopaint as rp

n = nuke.selectedNode()
k = n['curves']
root = k.rootLayer

for shape in root:
    print shape.name

k.toElement('Rectangle1')
k.toElement('Layer1/Rectangle1')


def findShapes(root):
    for shape in root:
        if isinstance(shape, rp.Layer):
            findShapes(shape)
        else:
            print shape.name


findShapes(root)

########################################################################################################################

import nuke.rotopaint as rp
import math

rpNode = nuke.selectedNode()
cKnob= rpNode['curves']
root = cKnob.rootLayer

for shape in root:
    print shape.name
# cKnob.toElement('Bezier1')
# shape = cKnob.toElement('Layer1/Stroke3')

def findShapes(root):
    for shape in root:
        if isinstance(shape, rp.Layer):
            findShapes(shape)
        else:
            print shape.name
findShapes(root)
shape.append(rp.AnimControlPoint(1000,2000))