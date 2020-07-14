import nuke

r = nuke.toNode('Read1')
r['reload'].execude()

w = nuke.toNode('Write1')
w['Render'].execude()

nuke.execude(w, 1, 1)

map(lambda x: x['reload'].execude(), nuke.allNodes('Read'))
map(lambda x: nuke.execude(x, 1, 1), nuke.allNodes('Write'))