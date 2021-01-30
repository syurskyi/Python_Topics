_____ ?
#read animation 
t = ?.selectedNode()
k = t['scale']
a = k.animations()
a = k.animation(0)
keys = a.keys()
keys[1].x
keys[1].y
a.setKey(10, 10)
# create animation
_____ math
r = t['rotate']
#variant 1
r.clearAnimated()
r.setAnimated()
___ i __ range(300):
    r.setValueAt(math.sin(i*0.07)*50, i, 0)
#vriant 2
r.clearAnimated()
r.setAnimated()
c = r.animation(0)
c.addKey( [?.AnimationKey(i, math.sin(i*0.07)*50) ___ i __ range(300)] )

#change one frame
c = r.animation(0)
key = c.keys()[21]

key.y = 50
r.setValueAt(40, 21,0)





