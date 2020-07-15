import nuke

root = nuke.toNode('root')
nuke.Root()

node = nuke.Root()
for k in node.allKnobs():
    print k.name()
    
node.addView('asd')

node.name() # 'Root' = not saved
node.modified()