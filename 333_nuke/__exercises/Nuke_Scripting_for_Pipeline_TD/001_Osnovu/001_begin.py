import nuke

# create  and connect nodes
r = nuke.createNode('Read', inpanel=False)
g = nuke.createNode('Grade', inpanel=False)
c = nuke.nodes.ColorCorrect(name='mainCC',xpos=400,ypos = 10, gain=2)
c.setInput(0, g)
c.autoplace()
b = nuke.nodes.Blur()
c.connectInput(1,b)
b.setInput(0, g)

no1, n02 = nuke.nodes.NoOp(),nuke.nodes.NoOp()
m = nuke.nodes.Merge(inputs=[no1, no2])

nuke.connectViewer(0,c)

# get node
sel = nuke.selectedNode()
sel = nuke.selectedNodes()
if sel:
    v = sel[0]
v = nuke.toNode('Viewer1')

v.canSetInput(0,c)
v.setInput(0, c)  

nuke.allNodes('ColorCorrect')
nuke.selectedNodes('ColorCorrect')

nodes = nuke.allNodes()
[ x for x in nodes if x.Class() == 'ColorCorrect']

nuke.activeViewer().node()


nuke.root()
nuke.toNode('preferences')

# knobs ######################################### 
# get value
nuke.toNode('Write2')['file'].getValue()
nuke.toNode('Write2')['file'].evaluate()
#set value 
import nuke
node = nuke.toNode('ColorCorrect2')
node['shadows.gain'].setValue(2)
node['channels'].setValue('rgba')

# link knobs
node['gain'].setExpression('%s.%s' % ('ColorCorrect1', 'gain'))
node['gain'].setExpression('shadows.gain * 2')

node['scale'].setExpression("[python nuke.frame()]")

n = nuke.toNode('Transform1')['scale'].setExpression('''[python -execlocal x = 2 
for i in range(100): 
    x += i 
ret = x]''')


# Move nodes
node = nuke.nodes.Transform()
node.autoplace()
nuke.autoplace(node)

node['xpos'].setValue(0)
n.setXYpos
nuke.zoomToFitSelected()
nuke.extractSelected()
