box = nuke.nodes.Cube()
geoNode = nuke.nodes.PythonGeo(inputs=[box])
g = geoNode['geo'].getGeometry()[0]
print dir(g)
print g.points()
print lens(g.points())
print lens(g.points())/3
print g.normals()
print len(g.normals())
print g.primitives()
print len(g.primitives())


########################################################################################################################

gbox = nuke.nodes.Cube()
geoNode = nuke.nodes.PythonGeo(inputs=[box])
g = geoNode['geo'].getGeometry()[0]
# dir(g)
# len(g.points())/3
# len(g.normals())/3
# len(g.primitives())
points = g.points()
points3 = []
for i in range(0, len(points), 3):
    v = (points[i], points[i+1], points[i+2])
    points3.append(v)
points3 = set(points3)

sp = nuke.nodes.Sphere()
m = nuke.nodes.MergeGeo()
for pt in points3:
    tr = nuke.nodes.TransformGeo(inputs=[sp])
    tr['translate'].setValue(pt)
    m.setInput(m.inputs()+1, tr)