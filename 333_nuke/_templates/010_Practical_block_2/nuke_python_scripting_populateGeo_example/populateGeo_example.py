______ ?
______ os, random

srcpath = 'C:/projects/src'

___ reorderPoints(array):
    data = []
    ___ i __ ra..(0, le.(array), 3):
        v = ?.math.Vector3(array[i], array[i+1], array[i+2])
        data.ap..(v)
    return data

geo, cam, scn = ?.selectedNodes()
pynode = ?.nodes.PythonGeo(inputs=[geo])
geoList = pynode.knob('geo').getGeometry()
points = []
___ elem __ geoList:
    points += elem.points()
points = reorderPoints(points)
?.delete(pynode)

grp = ?.nodes.Group(name='Objects')
grp.setXYpos(geo.xpos(), geo.ypos()+50)
scaleKnob = ?.Double_Knob('scale', 'Scale')
grp.addKnob(scaleKnob)
scaleKnob.sV..(0.5)

grp.begin()
inCam = ?.nodes.Input(name='LookAt')
out = ?.nodes.Output()

reads = []
___ img __ os.listdir(srcpath):
    path = os.path.join(srcpath, img).replace('\\','/')
    r = ?.nodes.Read(file=path, premultiplied=True)
    reads.ap..(r)

grpScene = ?.nodes.Scene(hide_input=True)
___ pt __ points:
    r = random.choice(reads)
    card = ?.nodes.Card(inputs=[r], rows = 1, columns=1,
    image_aspect=False, hide_input=True)
    tr = ?.nodes.TransformGeo(inputs=[card, None, inCam],
    xpos=card.xpos(), ypos=card.ypos()+40, hide_input=True)
    tr['translate'].sV..(pt)
    s = r.height()/float(r.width())
    tr['scaling'].sV..(s, 1)
    tr['uniform_scale'].setExpression('%s.scale' % grp.name())
    grpScene.setInput(grpScene.inputs(), tr)
    
out.setInput(0, grpScene)
    
grp.end()
grp.setInput(0, cam)
scn.setInput(0, grp)
    










