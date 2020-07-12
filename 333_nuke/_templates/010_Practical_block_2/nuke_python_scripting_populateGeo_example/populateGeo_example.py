______ ?
______ __, random

srcpath _ 'C:/projects/src'

___ reorderPoints(array):
    data _ []
    ___ i __ ra..(0, le.(array), 3):
        v _ ?.math.Vector3(array[i], array[i+1], array[i+2])
        data.ap..(v)
    r_ data

geo, cam, scn _ ?.sN..
pynode _ ?.nodes.PythonGeo(inputs_[geo])
geoList _ pynode.knob('geo').getGeometry()
points _ []
___ elem __ geoList:
    points +_ elem.points()
points _ reorderPoints(points)
?.delete(pynode)

grp _ ?.nodes.Group(name_'Objects')
grp.setXYpos(geo.xpos(), geo.ypos()+50)
scaleKnob _ ?.D_K..('scale', 'Scale')
grp.aK..(scaleKnob)
scaleKnob.sV..(0.5)

grp.begin()
inCam _ ?.nodes.Input(name_'LookAt')
out _ ?.nodes.Output()

reads _ []
___ img __ __.listdir(srcpath):
    path _ __.path.join(srcpath, img).r..('\\','/')
    r _ ?.nodes.Read(file_path, premultiplied_T..)
    reads.ap..(r)

grpScene _ ?.nodes.Scene(hide_input_T..)
___ pt __ points:
    r _ random.choice(reads)
    card _ ?.nodes.Card(inputs_[r], rows _ 1, columns_1,
    image_aspect_F.., hide_input_T..)
    tr _ ?.nodes.TransformGeo(inputs_[card, N.., inCam],
    xpos_card.xpos(), ypos_card.ypos()+40, hide_input_T..)
    tr['translate'].sV..(pt)
    s _ r.height()/float(r.width())
    tr['scaling'].sV..(s, 1)
    tr['uniform_scale'].setExpression('@.scale' % grp.name())
    grpScene.setInput(grpScene.inputs(), tr)
    
out.setInput(0, grpScene)
    
grp.end()
grp.setInput(0, cam)
scn.setInput(0, grp)
    










