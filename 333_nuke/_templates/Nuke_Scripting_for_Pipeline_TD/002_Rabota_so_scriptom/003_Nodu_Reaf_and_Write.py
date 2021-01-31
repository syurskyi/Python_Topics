_____ ?

r = ?.toNode('Read1')
r['reload'].execude()

w = ?.toNode('Write1')
w['Render'].execude()

?.execude(w, 1, 1)

map(lambda x: x['reload'].execude(), ?.aN..('Read'))
map(lambda x: ?.execude(x, 1, 1), ?.aN..('Write'))