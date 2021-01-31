#setup stereo
viewKnob _ ?.r__ .knob('views')
?.r__ .aV..('left')
?.aV..('right')
?.views()

viewKnob.toScript()
'left #00ff00\nright #ff0000'
viewKnob.fromScript( 'left #00ff00\nright #ff0000')

___ setUpMultiView( views_[ ('left',(0,1,0)), ('right',(1,0,0) ) ] ):
    newViews _ []
    ___ v __ views:   # CYCLE THROUGH EACH REQUESTED VIEW
        name _ v[0]   # GRAB THE CURRENT VIEWS NAME
        col _ v[1]    # GRAB THE CURRENT VIEWS COLOUR
        rgb _ tuple( [ in_(v*255) ___ v __ col ] ) #CONVERT FLOAT TO 8BIT INT AND RETURN A TUPLE
        hexCol _ '#%02x%02x%02x' % rgb             #CONVERT INTEGER NUMBERS TO HEX CODE
        curView _ '%s %s' % ( name, hexCol )       #COMBINE NAME AND HEX COLOUR TO SCRIPT SYNTAX
        newViews.a__( curView )      # COLLECT ALL REQUESTED VIEWS
    ?.r__ .knob('views').fromScript( '\n'.j..( newViews ) )
setUpMultiView()

n _ ?.cN..('Transform')
k _ n *t..
k.splitView()
k.sV..(1, 0,view_'right')
k.sV..(10, 0,view_'left')