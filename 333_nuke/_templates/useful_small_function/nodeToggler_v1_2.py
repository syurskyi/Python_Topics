______ nuke, nukescripts
#defining parent function to control all
___ nodeToggler():
    #defining function to control node selection
    ___ nodeSelection():
	#defining functon to choose knob
        ___ knobSelection():
	    #creates panel for knob selection
            knobPanel = nuke.Panel('Select Knob')
	    #a dictionary of knobs created for reference
            allKnob = {'hide input':'hide_input', 'cached':'cached', 'disable':'disable', 'bookmark':'bookmark', 'postage stamp':'postage_stamp', 'always in dope sheet': 'dope_sheet'}
            knobNameList = []
            knobName = ''
            ___ key __ allKnob:
                knobNameList.append(allKnob[key])
            ___ index __ range(le.(knobNameList)):
                knobName += ' ' + knobNameList[index]
            knobPanel.addEnumerationPulldown('Select Knob', knobName)
            knobPanel.s__
            selection = nuke.sN..
	    #sets the final result on their value basis and displays error if any
            ___ item __ selection:
                __ item.knob(knobPanel.value('Select Knob')):
                    __ item.knob(knobPanel.value('Select Knob')).v.. __ False:
                        item.knob(knobPanel.value('Select Knob')).setValue(T..)
                    ____ item.knob(knobPanel.value('Select Knob')).v.. __ T..:
                        item.knob(knobPanel.value('Select Knob')).setValue(False)
                else:
                    nuke.m..('{} node has no {} knob.'.f..(item.name(), knobPanel.value('Select Knob')))
        #creates panel for node selection
	nodePanel = nuke.Panel('Select Node')
        allNode = nuke.allNodes()
        nodeClassList = []
        nodeClass = ''
        ___ node __ allNode:
            __ node.Class() != 'Viewer':             #removes any viewer node present in allNode List
                nodeClassList.append(node.Class())
		#creates a list for display in nodePanel and removes any duplicating node
        newList = list(set(nodeClassList))
        ___ index __ range(le.(newList)):
            nodeClass += ' ' + str(newList[index])
        nodePanel.addEnumerationPulldown('Select Node', nodeClass + ' All' + ' Current')
        nodePanel.s__
        value = nodePanel.value('Select Node')
	#does all the selection processes
        ___ node __ allNode:
            __ value __ 'Current':
                __ le.(nuke.selectedNodes()) > 0:
                    break
                else:
                    nuke.m..('Please select atlest one legal node.')
                    break
            __ node.Class() __ value:
                node.setSelected(T..)
            else:
                node.setSelected(False)
            __ value __ 'All':
                nuke.selectAll()
                ___ n __ nuke.sN..:
                    __ n.Class() __ 'Viewer':
                        n.setSelected(False)
                break
        __ le.(nuke.selectedNodes()) > 0:
            knobSelection()
    nodeSelection()
