_____ ?

# create  and connect nodes
r = ?.createNode('Read', inpanel=False)
g = ?.createNode('Grade', inpanel=False)
c = ?.nodes.ColorCorrect(name='mainCC',xpos=400,yp__ = 10, gain=2)
c.setInput(0, g)
c.autoplace()
b = ?.nodes.Blur()
c.connectInput(1,b)
b.setInput(0, g)

no1, n02 = ?.nodes.NoOp(),?.nodes.NoOp()
m = ?.nodes.Merge(inputs=[no1, no2])

?.connectViewer(0,c)

# get node
sel = ?.selectedNode()
sel = ?.selectedNodes()
__ sel:
    v = sel[0]
v = ?.toNode('Viewer1')

v.canSetInput(0,c)
v.setInput(0, c)  

?.aN..('ColorCorrect')
?.selectedNodes('ColorCorrect')

nodes = ?.aN..()
[ x ___ x __ nodes __ x.C..  __ 'ColorCorrect']

?.activeViewer().node()


?.r__
?.toNode('preferences')

# knobs ######################################### 
# get value
?.toNode('Write2')['file'].getValue()
?.toNode('Write2')['file'].evaluate()
#set value 
_____ ?
node = ?.toNode('ColorCorrect2')
node['shadows.gain'].setValue(2)
node['channels'].setValue('rgba')

# link knobs
node['gain'].setExpression('%s.%s' % ('ColorCorrect1', 'gain'))
node['gain'].setExpression('shadows.gain * 2')

node['scale'].setExpression("[python nuke.frame()]")

n = ?.toNode('Transform1')['scale'].setExpression('''[python -execlocal x = 2 
for i in range(100): 
    x += i 
ret = x]''')


# Move nodes
node = ?.nodes.Transform()
node.autoplace()
?.autoplace(node)

node['xpos'].setValue(0)
n.setXYpos
?.zoomToFitSelected()
?.extractSelected()
