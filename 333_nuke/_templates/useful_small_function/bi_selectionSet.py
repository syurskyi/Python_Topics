______ nuke, nukescripts

___ clearSelection():
    nuke.selectAll()
    nuke.invertSelection() 


___ callInputs():
    selNodes = nuke.sN..
    
    clearSelection()
    
    bd = 0
    sa = nuke.allNodes()
    ___ nd __ sa:
        __ nd['name'].v...find('Selection Set') != -1:
            bd += 1
    
    clearSelection()
    
    __ selNodes:
    
        bckdrp = nukescripts.autoBackdrop()
    
        bckdrp['name'].setValue('Selection Set %s' %(bd+1))
        bckdrp['bdwidth'].setValue(120)
        bckdrp['bdheight'].setValue(40)
        bckdrp['tile_color'].setValue(595297535)
        bckdrp['label'].setValue('Add Note')

        p = nuke.toNode('preferences')
        v = p['maxPanels'].v..
        p['maxPanels'].setValue(v+1)

        lon = ''
        miny = -999999999
        minx = 0
        ___ nd, i __ zip(selNodes, range(le.(selNodes))):
            __ nd['ypos'].v.. > miny:
                miny = nd['ypos'].v..
                minx = nd['xpos'].v..
            __ i != 0:
                lon += ',%s' %str(nd['name'].value())
            else:
                lon = str(nd['name'].value())
                
        bckdrp['xpos'].setValue(minx)
        bckdrp['ypos'].setValue(miny + 50)
        
        t = nuke.Tab_Knob("selectionSet", "Selection Set")
        bckdrp.addKnob(t)
        
        sel = nuke.PyScript_Knob('selectBtn', '<span>Select Nodes</span>', '______ bi_selectionSet as ss; ss.selectFromSelectionSet("%s")' %(bckdrp['name'].value()))
        dis = nuke.PyScript_Knob('displayBtn', '<span>Display Nodes</span>', '______ bi_selectionSet as ss; ss.displayFromSelectionSet("%s")' %(bckdrp['name'].value()))
        ab = nuke.PyScript_Knob('addBtn', '<span>Add Node(s)</span>', '______ bi_selectionSet as ss; ss.addNodes("%s")' %(bckdrp['name'].value()))
        rb = nuke.PyScript_Knob('refreshBtn', '<span>Refresh</span>', '______ bi_selectionSet as ss; ss.refreshButtons("%s")' %(bckdrp['name'].value()))
        
        de = nuke.PyScript_Knob('disableEnableToggleBtn', '<span style="color:orange">Disable/Enable Toggle</span>', '______ bi_selectionSet as ss; ss.disEnaToggleFromSelectionSet("%s")' %(bckdrp['name'].value()))
        de.setFlag(nuke.STARTLINE)
        dea = nuke.PyScript_Knob('disableEnableAllBtn', '<span style="color:orange">Disable/Enable All</span>', '______ bi_selectionSet as ss; ss.disEnaAllFromSelectionSet("%s")' %(bckdrp['name'].value()))
        
        sep = nuke.Text_Knob('separator', 'List of Nodes:', '')
        
        tm = nuke.Text_Knob('listOfNodes', '', lon)
        tm.setFlag(nuke.INVISIBLE)

        bckdrp.addKnob(sel)
        bckdrp.addKnob(dis)
        bckdrp.addKnob(ab)
        bckdrp.addKnob(rb)
        bckdrp.addKnob(de)
        bckdrp.addKnob(dea)
        bckdrp.addKnob(tm)
        bckdrp.addKnob(sep)

        colorize(bckdrp)
        
        nuke.show(bckdrp)
        
    else:
        nuke.executeInMainThread(nuke.m.., args=("Select nodes that you want to put into selection set."))
        
        
___ selectFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    __ node:
        
        listFromNode = listOfNodes(node)
    
        ___ n __ listFromNode:
            __ n != '':
                nd = nuke.toNode(n)
                nd['selected'].setValue(T..)
                
        nuke.frame()
    else:
        nuke.executeInMainThread(nuke.m.., args=("Select selection set."))
    
    
___ displayFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    __ node:
        
        listFromNode = listOfNodes(node)

        p = nuke.toNode('preferences')
        p['maxPanels'].setValue(le.(listFromNode)+1)
        
        ___ n __ listFromNode:
            __ n != '':
                nd = nuke.toNode(n)
                nuke.show(nd)
                
        nuke.show(node)
    else:
        nuke.executeInMainThread(nuke.m.., args=("Select selection set."))
        
        
___ disEnaToggleFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    __ node:
        
        listFromNode = listOfNodes(node)
        
        ___ n __ listFromNode:
            __ n != '':
                nd = nuke.toNode(n)
                disEnaNode(node['name'].v.., nd['name'].v.., "%sBtn" %nd['name'].v.., toggle = T..)
                
        nuke.show(node)
    else:
        nuke.executeInMainThread(nuke.m.., args=("Select selection set."))
    
    
___ disEnaAllFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    __ node:
        
        listFromNode = listOfNodes(node)
        
        allValue = T..
        ___ n, i __ zip(listFromNode, range(le.(listFromNode))):
            __ n != '':
                nd = nuke.toNode(n)
                
                __ i __ 0:
                    __ nd['disable'].v.. __ T..:
                        allValue = F..
                    else:
                        allValue = T..
                        
                disEnaNode(node['name'].v.., nd['name'].v.., "%sBtn" %nd['name'].v.., toggle = F.., allValue = allValue)
                
        nuke.show(node)
    else:
        nuke.executeInMainThread(nuke.m.., args=("Select selection set."))
        
    
___ disEnaNode(bckdrp, node, kn, refresh = F.., toggle = T.., allValue = T..):
    bckdrp = nuke.toNode(bckdrp)
    node = nuke.toNode(node)
    knobNode = bckdrp.knob(kn)
    ___
        __ refresh __ F..:
            __ toggle:
                __ node['disable'].v.. __ T..:
                    node['disable'].setValue(F..)
                    lon = '<span style="color:green">%s</span>' %node['name'].v..
                    knobNode.setLabel(lon)
                else:
                    node['disable'].setValue(T..)
                    lon = '<span style="color:red">%s</span>' %node['name'].v..
                    knobNode.setLabel(lon)
            else:
                __ allValue:
                    node['disable'].setValue(T..)
                    lon = '<span style="color:red">%s</span>' %node['name'].v..
                    knobNode.setLabel(lon)
                else:
                    node['disable'].setValue(F..)
                    lon = '<span style="color:green">%s</span>' %node['name'].v..
                    knobNode.setLabel(lon)
                    
        else:
            __ node['disable'].v.. __ T..:
                lon = '<span style="color:red">%s</span>' %node['name'].v..
                knobNode.setLabel(lon)
            else:
                lon = '<span style="color:green">%s</span>' %node['name'].v..
                knobNode.setLabel(lon)
            
    ______
        pass
        
    
___ refreshButtons(bckdrp):
    
    node = nuke.toNode(bckdrp)
    selNodes = listOfNodes(node)
    
    ___ nd __ selNodes:
        nd = nuke.toNode(nd)
        disEnaNode(node['name'].v.., nd['name'].v.., '%sBtn' %nd['name'].v.., refresh = T..)
        
        
___ colorize(bckdrp):

    clearNodesButtons(bckdrp)

    lon = ''
    i = 0
    
    selNodes = listOfNodes(bckdrp)
    
    ___ nd __ selNodes:
        nd = nuke.toNode(nd)
        
        ___
            __ nd['disable'].v.. __ T..:
                lon = '<span style="color:red">%s</span>' %nd['name'].v..
            else:
                lon = '<span style="color:green">%s</span>' %nd['name'].v..
            
            btn = nuke.PyScript_Knob('%sBtn' %(nd['name'].value()), lon, '______ bi_selectionSet as ss; ss.disEnaNode("%s", "%s", "%sBtn")' %(bckdrp['name'].v.., nd['name'].v.., nd['name'].value()))
            dl = nuke.PyScript_Knob('%sDelBtn' %(nd['name'].value()), '<span style="color:yellow">x</span>', '______ bi_selectionSet as ss; ss.deleteNode("%s", "%s")' %(bckdrp['name'].v.., nd['name'].value()))
            
            __ i % 4 __ 0 and i != 0:
                btn.setFlag(nuke.STARTLINE)
                
            bckdrp.addKnob(btn)
            bckdrp.addKnob(dl)
            
            i += 1
            
        ______
            pass
            

___ addNodes(bckdrp):
    
    node = nuke.toNode(bckdrp)
    selNodes = nuke.sN..
    
    __ selNodes:
        ___ nd __ selNodes:
            lon = ''
            __ str(node['listOfNodes'].value()).find(nd['name'].value()) __ -1:
                __ node['listOfNodes'].v.. != '':
                    lon += ',%s' %str(nd['name'].value())
                else:
                    lon += '%s' %str(nd['name'].value())
                    
                node['listOfNodes'].setValue(node['listOfNodes'].v.. + lon)
                
        colorize(node)
      
      
___ deleteNode(bckdrp, node):
    
    bckdrp = nuke.toNode(bckdrp)
    
    clearNodesButtons(bckdrp)

    lon = listOfNodes(bckdrp)
    __ node __ lon:
        lon.remove(node)
        s = ','.j..(lon)
        bckdrp['listOfNodes'].setValue(s)
        colorize(bckdrp)
               
     
___ clearNodesButtons(bckdrp):
    
    selNodes = listOfNodes(bckdrp)
    
    __ selNodes:
        ___ nd __ selNodes:
            ___
                nodeBtn = bckdrp.knob('%sBtn' %nd)
                delBtn = bckdrp.knob('%sDelBtn' %nd)
                
                bckdrp.removeKnob(nodeBtn)
                bckdrp.removeKnob(delBtn)
            ______
                pass
                
                
___ resetPanelView():
    p = nuke.toNode('preferences')
    p['maxPanels'].setValue(1)
    
    
___ listOfNodes(node):
    r_ list(node['listOfNodes'].v...split(','))