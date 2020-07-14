import nuke

nuke.toNode('root')
nuke.root()
root = nuke.root()
root['fps'].setValue(30)
root['first_frame'].setValue(10)
root['last_frame'].setValue(200)

root.name()

root.modified()

root.firstFrame()
root.fps()
root.addView('left')
