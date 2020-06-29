box = ?.nodes.Cube()
geoNode = ?.nodes.PythonGeo(inputs=[box])
g = geoNode['geo'].getGeometry()[0]
print dir(g)
print g.points()
print lens(g.points())
print lens(g.points())/3
print g.normals()
print le.(g.normals())
print g.primitives()
print le.(g.primitives())


########################################################################################################################

gbox = ?.nodes.Cube()
geoNode = ?.nodes.PythonGeo(inputs=[box])
g = geoNode['geo'].getGeometry()[0]
# dir(g)
# len(g.points())/3
# len(g.normals())/3
# len(g.primitives())
points = g.points()
points3 = []
___ i __ ra..(0, le.(points), 3):
    v = (points[i], points[i+1], points[i+2])
    points3.ap..(v)
points3 = set(points3)

sp = ?.nodes.Sphere()
m = ?.nodes.MergeGeo()
___ pt __ points3:
    tr = ?.nodes.TransformGeo(inputs=[sp])
    tr['translate'].sV..(pt)
    m.setInput(m.inputs()+1, tr)