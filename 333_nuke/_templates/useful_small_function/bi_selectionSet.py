______ ?, nukescripts

___ clearSelection():
    ?.selectAll()
    ?.invertSelection() 


___ callInputs():
    selNodes _ ?.sN..
    
    clearSelection()
    
    bd _ 0
    sa _ ?.allNodes()
    ___ nd __ sa:
        __ nd['name'].v...find('Selection Set') !_ -1:
            bd +_ 1
    
    clearSelection()
    
    __ selNodes:
    
        bckdrp _ nukescripts.autoBackdrop()
    
        bckdrp['name'].setValue('Selection Set @' %(bd+1))
        bckdrp['bdwidth'].setValue(120)
        bckdrp['bdheight'].setValue(40)
        bckdrp['tile_color'].setValue(595297535)
        bckdrp['label'].setValue('Add Note')

        p _ ?.tN..('preferences')
        v _ p['maxPanels'].v..
        p['maxPanels'].setValue(v+1)

        lon _ ''
        miny _ -999999999
        minx _ 0
        ___ nd, i __ zip(selNodes, ra__(le.(selNodes))):
            __ nd['ypos'].v.. > miny:
                miny _ nd['ypos'].v..
                minx _ nd['xpos'].v..
            __ i !_ 0:
                lon +_ ',@' %st.(nd['name'].value())
            ____
                lon _ st.(nd['name'].value())
                
        bckdrp['xpos'].setValue(minx)
        bckdrp['ypos'].setValue(miny + 50)
        
        t _ ?.T_K..("selectionSet", "Selection Set")
        bckdrp.aK..(t)
        
        sel _ ?.PS_K..('selectBtn', '<span>Select Nodes</span>', '______ bi_selectionSet as ss; ss.selectFromSelectionSet("@")' %(bckdrp['name'].value()))
        dis _ ?.PS_K..('displayBtn', '<span>Display Nodes</span>', '______ bi_selectionSet as ss; ss.displayFromSelectionSet("@")' %(bckdrp['name'].value()))
        ab _ ?.PS_K..('addBtn', '<span>Add Node(s)</span>', '______ bi_selectionSet as ss; ss.addNodes("@")' %(bckdrp['name'].value()))
        rb _ ?.PS_K..('refreshBtn', '<span>Refresh</span>', '______ bi_selectionSet as ss; ss.refreshButtons("@")' %(bckdrp['name'].value()))
        
        de _ ?.PS_K..('disableEnableToggleBtn', '<span style="color:orange">Disable/Enable Toggle</span>', '______ bi_selectionSet as ss; ss.disEnaToggleFromSelectionSet("@")' %(bckdrp['name'].value()))
        de.sF..(?.ST..)
        dea _ ?.PS_K..('disableEnableAllBtn', '<span style="color:orange">Disable/Enable All</span>', '______ bi_selectionSet as ss; ss.disEnaAllFromSelectionSet("@")' %(bckdrp['name'].value()))
        
        sep _ ?.T_K..('separator', 'List of Nodes:', '')
        
        tm _ ?.T_K..('listOfNodes', '', lon)
        tm.sF..(?.IN..)

        bckdrp.aK..(sel)
        bckdrp.aK..(dis)
        bckdrp.aK..(ab)
        bckdrp.aK..(rb)
        bckdrp.aK..(de)
        bckdrp.aK..(dea)
        bckdrp.aK..(tm)
        bckdrp.aK..(sep)

        colorize(bckdrp)
        
        ?.show(bckdrp)
        
    ____
        ?.executeInMainThread(?.m.., args_("Select nodes that you want to put into selection set."))
        
        
___ selectFromSelectionSet(bckdrp):
    clearSelection()

    node _ ?.tN..(bckdrp)
    __ node:
        
        listFromNode _ listOfNodes(node)
    
        ___ n __ listFromNode:
            __ n !_ '':
                nd _ ?.tN..(n)
                nd['selected'].setValue(T..)
                
        ?.frame()
    ____
        ?.executeInMainThread(?.m.., args_("Select selection set."))
    
    
___ displayFromSelectionSet(bckdrp):
    clearSelection()

    node _ ?.tN..(bckdrp)
    __ node:
        
        listFromNode _ listOfNodes(node)

        p _ ?.tN..('preferences')
        p['maxPanels'].setValue(le.(listFromNode)+1)
        
        ___ n __ listFromNode:
            __ n !_ '':
                nd _ ?.tN..(n)
                ?.show(nd)
                
        ?.show(node)
    ____
        ?.executeInMainThread(?.m.., args_("Select selection set."))
        
        
___ disEnaToggleFromSelectionSet(bckdrp):
    clearSelection()

    node _ ?.tN..(bckdrp)
    __ node:
        
        listFromNode _ listOfNodes(node)
        
        ___ n __ listFromNode:
            __ n !_ '':
                nd _ ?.tN..(n)
                disEnaNode(node['name'].v.., nd['name'].v.., "%sBtn" %nd['name'].v.., toggle _ T..)
                
        ?.show(node)
    ____
        ?.executeInMainThread(?.m.., args_("Select selection set."))
    
    
___ disEnaAllFromSelectionSet(bckdrp):
    clearSelection()

    node _ ?.tN..(bckdrp)
    __ node:
        
        listFromNode _ listOfNodes(node)
        
        allValue _ T..
        ___ n, i __ zip(listFromNode, ra__(le.(listFromNode))):
            __ n !_ '':
                nd _ ?.tN..(n)
                
                __ i __ 0:
                    __ nd['disable'].v.. __ T..:
                        allValue _ F..
                    ____
                        allValue _ T..
                        
                disEnaNode(node['name'].v.., nd['name'].v.., "%sBtn" %nd['name'].v.., toggle _ F.., allValue _ allValue)
                
        ?.show(node)
    ____
        ?.executeInMainThread(?.m.., args_("Select selection set."))
        
    
___ disEnaNode(bckdrp, node, kn, refresh _ F.., toggle _ T.., allValue _ T..):
    bckdrp _ ?.tN..(bckdrp)
    node _ ?.tN..(node)
    knobNode _ bckdrp.knob(kn)
    ___
        __ refresh __ F..:
            __ toggle:
                __ node['disable'].v.. __ T..:
                    node['disable'].setValue(F..)
                    lon _ '<span style="color:green">@</span>' %node['name'].v..
                    knobNode.sL..(lon)
                ____
                    node['disable'].setValue(T..)
                    lon _ '<span style="color:red">@</span>' %node['name'].v..
                    knobNode.sL..(lon)
            ____
                __ allValue:
                    node['disable'].setValue(T..)
                    lon _ '<span style="color:red">@</span>' %node['name'].v..
                    knobNode.sL..(lon)
                ____
                    node['disable'].setValue(F..)
                    lon _ '<span style="color:green">@</span>' %node['name'].v..
                    knobNode.sL..(lon)
                    
        ____
            __ node['disable'].v.. __ T..:
                lon _ '<span style="color:red">@</span>' %node['name'].v..
                knobNode.sL..(lon)
            ____
                lon _ '<span style="color:green">@</span>' %node['name'].v..
                knobNode.sL..(lon)
            
    ______
        p..
        
    
___ refreshButtons(bckdrp):
    
    node _ ?.tN..(bckdrp)
    selNodes _ listOfNodes(node)
    
    ___ nd __ selNodes:
        nd _ ?.tN..(nd)
        disEnaNode(node['name'].v.., nd['name'].v.., '%sBtn' %nd['name'].v.., refresh _ T..)
        
        
___ colorize(bckdrp):

    clearNodesButtons(bckdrp)

    lon _ ''
    i _ 0
    
    selNodes _ listOfNodes(bckdrp)
    
    ___ nd __ selNodes:
        nd _ ?.tN..(nd)
        
        ___
            __ nd['disable'].v.. __ T..:
                lon _ '<span style="color:red">@</span>' %nd['name'].v..
            ____
                lon _ '<span style="color:green">@</span>' %nd['name'].v..
            
            btn _ ?.PS_K..('%sBtn' %(nd['name'].value()), lon, '______ bi_selectionSet as ss; ss.disEnaNode("@", "@", "%sBtn")' %(bckdrp['name'].v.., nd['name'].v.., nd['name'].value()))
            dl _ ?.PS_K..('%sDelBtn' %(nd['name'].value()), '<span style="color:yellow">x</span>', '______ bi_selectionSet as ss; ss.deleteNode("@", "@")' %(bckdrp['name'].v.., nd['name'].value()))
            
            __ i % 4 __ 0 an. i !_ 0:
                btn.sF..(?.ST..)
                
            bckdrp.aK..(btn)
            bckdrp.aK..(dl)
            
            i +_ 1
            
        ______
            p..
            

___ addNodes(bckdrp):
    
    node _ ?.tN..(bckdrp)
    selNodes _ ?.sN..
    
    __ selNodes:
        ___ nd __ selNodes:
            lon _ ''
            __ st.(node['listOfNodes'].value()).find(nd['name'].value()) __ -1:
                __ node['listOfNodes'].v.. !_ '':
                    lon +_ ',@' %st.(nd['name'].value())
                ____
                    lon +_ '@' %st.(nd['name'].value())
                    
                node['listOfNodes'].setValue(node['listOfNodes'].v.. + lon)
                
        colorize(node)
      
      
___ deleteNode(bckdrp, node):
    
    bckdrp _ ?.tN..(bckdrp)
    
    clearNodesButtons(bckdrp)

    lon _ listOfNodes(bckdrp)
    __ node __ lon:
        lon.remove(node)
        s _ ','.j..(lon)
        bckdrp['listOfNodes'].setValue(s)
        colorize(bckdrp)
               
     
___ clearNodesButtons(bckdrp):
    
    selNodes _ listOfNodes(bckdrp)
    
    __ selNodes:
        ___ nd __ selNodes:
            ___
                nodeBtn _ bckdrp.knob('%sBtn' %nd)
                delBtn _ bckdrp.knob('%sDelBtn' %nd)
                
                bckdrp.removeKnob(nodeBtn)
                bckdrp.removeKnob(delBtn)
            ______
                p..
                
                
___ resetPanelView():
    p _ ?.tN..('preferences')
    p['maxPanels'].setValue(1)
    
    
___ listOfNodes(node):
    r_ list(node['listOfNodes'].v...s..(','))