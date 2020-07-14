import nuke
import os, random

srcpath = 'C:/projects/src'

def reorderPoints(array):
    data = []
    for i in range(0, len(array), 3):
        v = nuke.math.Vector3(array[i], array[i+1], array[i+2])
        data.append(v)
    return data

geo, cam, scn = nuke.selectedNodes()
pynode = nuke.nodes.PythonGeo(inputs=[geo])
geoList = pynode.knob('geo').getGeometry()
points = []
for elem in geoList:
    points += elem.points()
points = reorderPoints(points)
nuke.delete(pynode)    

grp = nuke.nodes.Group(name='Objects')
grp.setXYpos(geo.xpos(), geo.ypos()+50)
scaleKnob = nuke.Double_Knob('scale', 'Scale')
grp.addKnob(scaleKnob)
scaleKnob.setValue(0.5)

grp.begin()
inCam = nuke.nodes.Input(name='LookAt')
out = nuke.nodes.Output()

reads = []
for img in os.listdir(srcpath):
    path = os.path.join(srcpath, img).replace('\\','/')
    r = nuke.nodes.Read(file=path, premultiplied=True)
    reads.append(r)

grpScene = nuke.nodes.Scene(hide_input=True)
for pt in points:
    r = random.choice(reads)
    card = nuke.nodes.Card(inputs=[r], rows = 1, columns=1,
    image_aspect=False, hide_input=True)
    tr = nuke.nodes.TransformGeo(inputs=[card, None, inCam],
    xpos=card.xpos(), ypos=card.ypos()+40, hide_input=True)
    tr['translate'].setValue(pt)
    s = r.height()/float(r.width())
    tr['scaling'].setValue(s, 1)
    tr['uniform_scale'].setExpression('%s.scale' % grp.name())
    grpScene.setInput(grpScene.inputs(), tr)
    
out.setInput(0, grpScene)
    
grp.end()
grp.setInput(0, cam)
scn.setInput(0, grp)
    










