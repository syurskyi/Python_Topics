#setup stereo
viewKnob = nuke.root().knob('views')
nuke.root().addView('left')
nuke.addView('right')
nuke.views()

viewKnob.toScript()
'left #00ff00\nright #ff0000'
viewKnob.fromScript( 'left #00ff00\nright #ff0000')

def setUpMultiView( views=[ ('left',(0,1,0)), ('right',(1,0,0) ) ] ):
    newViews = []
    for v in views:   # CYCLE THROUGH EACH REQUESTED VIEW
        name = v[0]   # GRAB THE CURRENT VIEWS NAME
        col = v[1]    # GRAB THE CURRENT VIEWS COLOUR
        rgb = tuple( [ int(v*255) for v in col ] ) #CONVERT FLOAT TO 8BIT INT AND RETURN A TUPLE
        hexCol = '#%02x%02x%02x' % rgb             #CONVERT INTEGER NUMBERS TO HEX CODE
        curView = '%s %s' % ( name, hexCol )       #COMBINE NAME AND HEX COLOUR TO SCRIPT SYNTAX
        newViews.append( curView )      # COLLECT ALL REQUESTED VIEWS
    nuke.root().knob('views').fromScript( '\n'.join( newViews ) )
setUpMultiView()

n = nuke.createNode('Transform')
k = n['translate']
k.splitView()
k.setValue(1, 0,view='right')
k.setValue(10, 0,view='left')