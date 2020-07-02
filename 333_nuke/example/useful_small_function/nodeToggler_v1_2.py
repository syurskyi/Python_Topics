import nuke, nukescripts
#defining parent function to control all
def nodeToggler():
    #defining function to control node selection
    def nodeSelection():
	#defining functon to choose knob
        def knobSelection():
	    #creates panel for knob selection
            knobPanel = nuke.Panel('Select Knob')
	    #a dictionary of knobs created for reference
            allKnob = {'hide input':'hide_input', 'cached':'cached', 'disable':'disable', 'bookmark':'bookmark', 'postage stamp':'postage_stamp', 'always in dope sheet': 'dope_sheet'}
            knobNameList = []
            knobName = ''
            for key in allKnob:
                knobNameList.append(allKnob[key])
            for index in range(len(knobNameList)):
                knobName += ' ' + knobNameList[index]
            knobPanel.addEnumerationPulldown('Select Knob', knobName)
            knobPanel.show()
            selection = nuke.selectedNodes()
	    #sets the final result on their value basis and displays error if any
            for item in selection:
                if item.knob(knobPanel.value('Select Knob')):
                    if item.knob(knobPanel.value('Select Knob')).value() == False:
                        item.knob(knobPanel.value('Select Knob')).setValue(True)
                    elif item.knob(knobPanel.value('Select Knob')).value() == True:
                        item.knob(knobPanel.value('Select Knob')).setValue(False)
                else:
                    nuke.message('{} node has no {} knob.'.format(item.name(), knobPanel.value('Select Knob')))
        #creates panel for node selection
	nodePanel = nuke.Panel('Select Node')
        allNode = nuke.allNodes()
        nodeClassList = []
        nodeClass = ''
        for node in allNode:
            if node.Class() != 'Viewer':             #removes any viewer node present in allNode List
                nodeClassList.append(node.Class())
		#creates a list for display in nodePanel and removes any duplicating node
        newList = list(set(nodeClassList))
        for index in range(len(newList)):
            nodeClass += ' ' + str(newList[index])
        nodePanel.addEnumerationPulldown('Select Node', nodeClass + ' All' + ' Current')
        nodePanel.show()
        value = nodePanel.value('Select Node')
	#does all the selection processes
        for node in allNode:
            if value == 'Current':
                if len(nuke.selectedNodes()) > 0:
                    break
                else:
                    nuke.message('Please select atlest one legal node.')
                    break
            if node.Class() == value:
                node.setSelected(True)
            else:
                node.setSelected(False)
            if value == 'All':
                nuke.selectAll()
                for n in nuke.selectedNodes():
                    if n.Class() == 'Viewer':
                        n.setSelected(False)
                break
        if len(nuke.selectedNodes()) > 0:
            knobSelection()
    nodeSelection()
