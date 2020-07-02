import nuke, nukescripts

def clearSelection():
    nuke.selectAll()
    nuke.invertSelection() 


def callInputs():
    selNodes = nuke.selectedNodes()
    
    clearSelection()
    
    bd = 0
    sa = nuke.allNodes()
    for nd in sa:
        if nd['name'].value().find('Selection Set') != -1:
            bd += 1
    
    clearSelection()
    
    if selNodes:
    
        bckdrp = nukescripts.autoBackdrop()
    
        bckdrp['name'].setValue('Selection Set %s' %(bd+1))
        bckdrp['bdwidth'].setValue(120)
        bckdrp['bdheight'].setValue(40)
        bckdrp['tile_color'].setValue(595297535)
        bckdrp['label'].setValue('Add Note')

        p = nuke.toNode('preferences')
        v = p['maxPanels'].value()
        p['maxPanels'].setValue(v+1)

        lon = ''
        miny = -999999999
        minx = 0
        for nd, i in zip(selNodes, range(len(selNodes))):
            if nd['ypos'].value() > miny:
                miny = nd['ypos'].value()
                minx = nd['xpos'].value()
            if i != 0:
                lon += ',%s' %str(nd['name'].value())
            else:
                lon = str(nd['name'].value())
                
        bckdrp['xpos'].setValue(minx)
        bckdrp['ypos'].setValue(miny + 50)
        
        t = nuke.Tab_Knob("selectionSet", "Selection Set")
        bckdrp.addKnob(t)
        
        sel = nuke.PyScript_Knob('selectBtn', '<span>Select Nodes</span>', 'import bi_selectionSet as ss; ss.selectFromSelectionSet("%s")' %(bckdrp['name'].value()))
        dis = nuke.PyScript_Knob('displayBtn', '<span>Display Nodes</span>', 'import bi_selectionSet as ss; ss.displayFromSelectionSet("%s")' %(bckdrp['name'].value()))
        ab = nuke.PyScript_Knob('addBtn', '<span>Add Node(s)</span>', 'import bi_selectionSet as ss; ss.addNodes("%s")' %(bckdrp['name'].value()))
        rb = nuke.PyScript_Knob('refreshBtn', '<span>Refresh</span>', 'import bi_selectionSet as ss; ss.refreshButtons("%s")' %(bckdrp['name'].value()))
        
        de = nuke.PyScript_Knob('disableEnableToggleBtn', '<span style="color:orange">Disable/Enable Toggle</span>', 'import bi_selectionSet as ss; ss.disEnaToggleFromSelectionSet("%s")' %(bckdrp['name'].value()))
        de.setFlag(nuke.STARTLINE)
        dea = nuke.PyScript_Knob('disableEnableAllBtn', '<span style="color:orange">Disable/Enable All</span>', 'import bi_selectionSet as ss; ss.disEnaAllFromSelectionSet("%s")' %(bckdrp['name'].value()))
        
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
        nuke.executeInMainThread(nuke.message, args=("Select nodes that you want to put into selection set."))
        
        
def selectFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    if node:
        
        listFromNode = listOfNodes(node)
    
        for n in listFromNode:
            if n != '':
                nd = nuke.toNode(n)
                nd['selected'].setValue(True)
                
        nuke.frame()
    else:
        nuke.executeInMainThread(nuke.message, args=("Select selection set."))
    
    
def displayFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    if node:
        
        listFromNode = listOfNodes(node)

        p = nuke.toNode('preferences')
        p['maxPanels'].setValue(len(listFromNode)+1)
        
        for n in listFromNode:
            if n != '':
                nd = nuke.toNode(n)
                nuke.show(nd)
                
        nuke.show(node)
    else:
        nuke.executeInMainThread(nuke.message, args=("Select selection set."))
        
        
def disEnaToggleFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    if node:
        
        listFromNode = listOfNodes(node)
        
        for n in listFromNode:
            if n != '':
                nd = nuke.toNode(n)
                disEnaNode(node['name'].value(), nd['name'].value(), "%sBtn" %nd['name'].value(), toggle = True)
                
        nuke.show(node)
    else:
        nuke.executeInMainThread(nuke.message, args=("Select selection set."))
    
    
def disEnaAllFromSelectionSet(bckdrp):
    clearSelection()

    node = nuke.toNode(bckdrp)
    if node:
        
        listFromNode = listOfNodes(node)
        
        allValue = True
        for n, i in zip(listFromNode, range(len(listFromNode))):
            if n != '':
                nd = nuke.toNode(n)
                
                if i == 0:
                    if nd['disable'].value() == True:
                        allValue = False
                    else:
                        allValue = True
                        
                disEnaNode(node['name'].value(), nd['name'].value(), "%sBtn" %nd['name'].value(), toggle = False, allValue = allValue)
                
        nuke.show(node)
    else:
        nuke.executeInMainThread(nuke.message, args=("Select selection set."))
        
    
def disEnaNode(bckdrp, node, kn, refresh = False, toggle = True, allValue = True):
    bckdrp = nuke.toNode(bckdrp)
    node = nuke.toNode(node)
    knobNode = bckdrp.knob(kn)
    try:
        if refresh is False:
            if toggle:
                if node['disable'].value() == True:
                    node['disable'].setValue(False)
                    lon = '<span style="color:green">%s</span>' %node['name'].value()
                    knobNode.setLabel(lon)
                else:
                    node['disable'].setValue(True)
                    lon = '<span style="color:red">%s</span>' %node['name'].value()
                    knobNode.setLabel(lon)
            else:
                if allValue:
                    node['disable'].setValue(True)
                    lon = '<span style="color:red">%s</span>' %node['name'].value()
                    knobNode.setLabel(lon)
                else:
                    node['disable'].setValue(False)
                    lon = '<span style="color:green">%s</span>' %node['name'].value()
                    knobNode.setLabel(lon)
                    
        else:
            if node['disable'].value() == True:
                lon = '<span style="color:red">%s</span>' %node['name'].value()
                knobNode.setLabel(lon)
            else:
                lon = '<span style="color:green">%s</span>' %node['name'].value()
                knobNode.setLabel(lon)
            
    except:
        pass
        
    
def refreshButtons(bckdrp):
    
    node = nuke.toNode(bckdrp)
    selNodes = listOfNodes(node)
    
    for nd in selNodes:
        nd = nuke.toNode(nd)
        disEnaNode(node['name'].value(), nd['name'].value(), '%sBtn' %nd['name'].value(), refresh = True)
        
        
def colorize(bckdrp):

    clearNodesButtons(bckdrp)

    lon = ''
    i = 0
    
    selNodes = listOfNodes(bckdrp)
    
    for nd in selNodes:
        nd = nuke.toNode(nd)
        
        try:
            if nd['disable'].value() == True:
                lon = '<span style="color:red">%s</span>' %nd['name'].value()
            else:
                lon = '<span style="color:green">%s</span>' %nd['name'].value()
            
            btn = nuke.PyScript_Knob('%sBtn' %(nd['name'].value()), lon, 'import bi_selectionSet as ss; ss.disEnaNode("%s", "%s", "%sBtn")' %(bckdrp['name'].value(), nd['name'].value(), nd['name'].value()))
            dl = nuke.PyScript_Knob('%sDelBtn' %(nd['name'].value()), '<span style="color:yellow">x</span>', 'import bi_selectionSet as ss; ss.deleteNode("%s", "%s")' %(bckdrp['name'].value(), nd['name'].value()))
            
            if i % 4 == 0 and i != 0:
                btn.setFlag(nuke.STARTLINE)
                
            bckdrp.addKnob(btn)
            bckdrp.addKnob(dl)
            
            i += 1
            
        except:
            pass
            

def addNodes(bckdrp):
    
    node = nuke.toNode(bckdrp)
    selNodes = nuke.selectedNodes()
    
    if selNodes:
        for nd in selNodes:
            lon = ''
            if str(node['listOfNodes'].value()).find(nd['name'].value()) == -1:
                if node['listOfNodes'].value() != '':
                    lon += ',%s' %str(nd['name'].value())
                else:
                    lon += '%s' %str(nd['name'].value())
                    
                node['listOfNodes'].setValue(node['listOfNodes'].value() + lon)
                
        colorize(node)
      
      
def deleteNode(bckdrp, node):
    
    bckdrp = nuke.toNode(bckdrp)
    
    clearNodesButtons(bckdrp)

    lon = listOfNodes(bckdrp)
    if node in lon:
        lon.remove(node)
        s = ','.join(lon)
        bckdrp['listOfNodes'].setValue(s)
        colorize(bckdrp)
               
     
def clearNodesButtons(bckdrp):
    
    selNodes = listOfNodes(bckdrp)
    
    if selNodes:
        for nd in selNodes:
            try:
                nodeBtn = bckdrp.knob('%sBtn' %nd)
                delBtn = bckdrp.knob('%sDelBtn' %nd)
                
                bckdrp.removeKnob(nodeBtn)
                bckdrp.removeKnob(delBtn)
            except:
                pass
                
                
def resetPanelView():
    p = nuke.toNode('preferences')
    p['maxPanels'].setValue(1)
    
    
def listOfNodes(node):
    return list(node['listOfNodes'].value().split(','))