n = nuke.selectedNode()
n.sample(1, 616, 462)

n.sample('green', 299, 370, 10, 10)

[n.sample(x,309, 98) for x in 1,2,3]+[1]

color = [n.sample(x,309, 98) for x in 1,2,3]+[1]
c =nuke.nuke.nodes.Constant()
c['color'].setValue(color)

n = nuke.selectedNode()
colors = []
for i in range(0,n.height(), 10):
    for j in range(0,n.width(),10):
        colors.append([n.sample(x,i, j) for x in [1,2,3]])

color = [sum(x)/len(x) for x in zip(*colors)]
c = nuke.nodes.Constant()
c['color'].setValue(color+[1])

########################################################################################################################

# sample pixel
n = nuke.selectedNode()
c = nuke.nodes.Constant()
c['color'].setValue([n.sample(x,325, 355) for x in 1,2,3]+[1])



# Average color

n = nuke.selectedNode()
colors = []
for i in range(0,n.height(), 10):
    for j in range(0,n.width(),10):
        colors.append([n.sample(x,i, j) for x in [1,2,3]])

color = [sum(x)/len(x) for x in zip(*colors)]
c = nuke.nodes.Constant()
c['color'].setValue(color+[1])