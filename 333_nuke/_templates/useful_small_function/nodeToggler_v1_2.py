______ ?, nukescripts
#defining parent function to control all
___ nodeToggler():
    #defining function to control node selection
    ___ nodeSelection():
	#defining functon to choose knob
        ___ knobSelection():
	    #creates panel for knob selection
            knobPanel _ ?.Panel('Select Knob')
	    #a dictionary of knobs created for reference
            allKnob _ {'hide input':'hide_input', 'cached':'cached', 'disable':'disable', 'bookmark':'bookmark', 'postage stamp':'postage_stamp', 'always in dope sheet': 'dope_sheet'}
            knobNameList _ # list
            knobName _ ''
            ___ key __ allKnob:
                knobNameList.append(allKnob[key])
            ___ index __ ra__(le.(knobNameList)):
                knobName +_ ' ' + knobNameList[index]
            knobPanel.addEnumerationPulldown('Select Knob', knobName)
            knobPanel.s__
            selection _ ?.sN..
	    #sets the final result on their value basis and displays error if any
            ___ item __ selection:
                __ item.knob(knobPanel.value('Select Knob')):
                    __ item.knob(knobPanel.value('Select Knob')).v.. __ F..:
                        item.knob(knobPanel.value('Select Knob')).setValue(T..)
                    ____ item.knob(knobPanel.value('Select Knob')).v.. __ T..:
                        item.knob(knobPanel.value('Select Knob')).setValue(F..)
                ____
                    ?.m..('{} node has no {} knob.'.f..(item.name(), knobPanel.value('Select Knob')))
        #creates panel for node selection
	nodePanel _ ?.Panel('Select Node')
        allNode _ ?.allNodes()
        nodeClassList _ # list
        nodeClass _ ''
        ___ node __ allNode:
            __ node.Class() !_ 'Viewer':             #removes any viewer node present in allNode List
                nodeClassList.append(node.Class())
		#creates a list for display in nodePanel and removes any duplicating node
        newList _ list(set(nodeClassList))
        ___ index __ ra__(le.(newList)):
            nodeClass +_ ' ' + st.(newList[index])
        nodePanel.addEnumerationPulldown('Select Node', nodeClass + ' All' + ' Current')
        nodePanel.s__
        value _ nodePanel.value('Select Node')
	#does all the selection processes
        ___ node __ allNode:
            __ value __ 'Current':
                __ le.(?.sN..()) > 0:
                    break
                ____
                    ?.m..('Please select atlest one legal node.')
                    break
            __ node.Class() __ value:
                node.setSelected(T..)
            ____
                node.setSelected(F..)
            __ value __ 'All':
                ?.selectAll()
                ___ n __ ?.sN..:
                    __ n.Class() __ 'Viewer':
                        n.setSelected(F..)
                break
        __ le.(?.sN..()) > 0:
            knobSelection()
    nodeSelection()
