#setup stereo
viewKnob = ?.r__ .knob('views')
?.r__ .addView('left')
?.addView('right')
?.views()

viewKnob.toScript()
'left #00ff00\nright #ff0000'
viewKnob.fromScript( 'left #00ff00\nright #ff0000')

___ setUpMultiView( views=[ ('left',(0,1,0)), ('right',(1,0,0) ) ] ):
    newViews = []
    ___ v __ views:   # CYCLE THROUGH EACH REQUESTED VIEW
        name = v[0]   # GRAB THE CURRENT VIEWS NAME
        col = v[1]    # GRAB THE CURRENT VIEWS COLOUR
        rgb = tuple( [ int(v*255) ___ v __ col ] ) #CONVERT FLOAT TO 8BIT INT AND RETURN A TUPLE
        hexCol = '#%02x%02x%02x' % rgb             #CONVERT INTEGER NUMBERS TO HEX CODE
        curView = '%s %s' % ( name, hexCol )       #COMBINE NAME AND HEX COLOUR TO SCRIPT SYNTAX
        newViews.a__( curView )      # COLLECT ALL REQUESTED VIEWS
    ?.r__ .knob('views').fromScript( '\n'.join( newViews ) )
setUpMultiView()

n = ?.createNode('Transform')
k = n['translate']
k.splitView()
k.setValue(1, 0,view='right')
k.setValue(10, 0,view='left')