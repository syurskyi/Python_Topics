import ?.rotopaint as rp

n = ?.sN__
k = n['curves']
root = k.rootLayer

___ shape __ root:
    print shape.name

k.toElement('Rectangle1')
k.toElement('Layer1/Rectangle1')


def findShapes(root):
    ___ shape __ root:
        if isinstance(shape, rp.Layer):
            findShapes(shape)
        else:
            print shape.name


findShapes(root)

########################################################################################################################

import ?.rotopaint as rp
import math

rpNode = ?.sN__
cKnob= rpNode['curves']
root = cKnob.rootLayer

___ shape __ root:
    print shape.name
# cKnob.toElement('Bezier1')
# shape = cKnob.toElement('Layer1/Stroke3')

def findShapes(root):
    ___ shape __ root:
        if isinstance(shape, rp.Layer):
            findShapes(shape)
        else:
            print shape.name
findShapes(root)
shape.ap..(rp.AnimControlPoint(1000,2000))