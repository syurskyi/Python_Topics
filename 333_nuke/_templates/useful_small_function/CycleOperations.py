# Max van Leeuwen - maxvanleeuwen.com
# CycleOperations - 1.5
#
#
#
# The most-used knob of the selected node will cycle through its options, forwards or backwards (depending on the used keyboard shortcut).
# You won't have to open the properties box for the following nodes if you're only changing these knobs:
#
# Merge, ChannelMerge, and MergeMat will scroll through all merge operations. If you added items to the custom lists for these nodes, the nodes will only scroll through those!
# Switch will scroll through the node's inputs.
# Colorspace and OCIOColorspace will swap the in and out colourspaces.
# Shuffle will cycle the 'in' knob, and a label will display the current state.
# Keyer will cycle the 'operation' knob.
# FrameHold will increase or decrease the 'first_frame' knob value.
# Invert, Multiply, Blur, and Grade will cycle through the 'channels' knob.
# Log2Lin toggles log2lin and lin2log.
#
#
#
#
# Operation list example: ['minus', 'multiply', 'over', 'plus', 'screen']


C_Merge = []
C_ChannelMerge = []
C_MergeMat = []



#########################################


# TODO fix cycleoperations is other way around with valuemask, check blur or grade



_____ ?




___ Merge(n, cycle, forwards):

	___

		# get knob
		k = n.knob('operation')


		# if custom list is used
		__ le.(cycle) > 0:

			# get knob value as str
			currOp = k.v.. ()

			# check if current value is in cycle
			nextOp = ''

			__ currOp __ cycle:

				# get next or pevious item index (depending on forwards)
				index = cycle.index(currOp) + (1 __ forwards else -1)

				# return to 0 if out of range
				__(index > (le.(cycle)) - 1):
					index = 0

				# set new value
				nextOp = cycle[index]
			else:

				# reset to first in cycle
				nextOp = cycle[0]

			# set new value to knob
			n.knob("operation").sV..(nextOp)


		# if not, simply scroll through all options
		else:

			# current operation
			currOp = k.gV..

			# operation count
			countOp = le.(k.values())

			__ forwards:

				# if last item in list, go to start
				__ int(currOp) + 1 __ countOp:
					k.sV..(0)

				else:
					k.sV..(int(currOp) + 1)

			else:

				__ currOp __ 0:
					k.sV..(countOp - 1)
				else:
					k.sV..(int(currOp) - 1)

	______

		pass



___ Switch(n, forwards):

	___

		# get current value
		currWhich = n.knob('which').gV..
		# get amount of inputs on Switch (-1, to match input index which starts counting at 0)
		maxWhich = n.inputs() - 1.0

		# make Switch nodes with only one input alternate between 1 and 0
		__(maxWhich __ 0):
			maxWhich = 1

		# new value for Which on Switch
		newWhich = -1.0
		__ forwards:

			newWhich = currWhich + 1.0
			__ maxWhich < newWhich:
				newWhich = 0.0

		else:

			newWhich = currWhich - 1.0
			__ newWhich < 0.0:
				newWhich = maxWhich

		n.knob('which').sV..(newWhich)

	______

		pass



___ OCIOColorSpace(n):

	___

		# get knobs
		k1 = n.knob('in_colorspace')
		k2 = n.knob('out_colorspace')

		# get values
		inC = k1.v.. ()
		outC = k2.v.. ()

		# set inverse values
		k1.sV..(outC)
		k2.sV..(inC)

	______

		pass



___ Shuffle(n, forwards):

	___

		# get knob
		k = n.knob('in')

		# get current layer (str)
		currL = k.v.. ()

		# get all existing layers
		listL = ?.layers()

		# get index of current layer
		i = 0
		___ eachL __ listL:
			__ eachL __ currL:
				break
			i += 1

		# get new layer
		__ forwards:

			__ le.(listL) __ i + 1:
				newL = listL[0]
			else:
				newL = listL[i + 1]

		else:

			__ i __ 0:
				newL = listL[le.(listL) - 1]
			else:
				newL = listL[i - 1]


		# set new layer
		k.sV..(newL)


		# set label
		giveLabel(n, 'in')

	______

		pass



___ FrameHold(n, forwards):

	___

		# get knob
		k = n.knob('first_frame')

		# get current frame
		currF = k.gV..

		# next value
		newF = currF + 1 __ forwards else currF - 1

		# set new value
		k.sV..(newF)

	______

		pass



___ anyChannelKnob(n, knobName, forwards):

	___

		# get knob
		k = n.knob(knobName)

		# get knob value (str)
		currL = k.v.. ()

		# get all possible layers
		listL = ?.layers()
		listL.insert(0, 'all')
		listL.insert(1, 'none')

		# get index of current layer
		i = 0
		___ eachL __ listL:
			__ eachL __ currL:
				break
			i += 1



		# get new layer
		__ forwards:

			__ le.(listL) __ i + 1:
				newL = listL[0]
			else:
				newL = listL[i + 1]

		else:

			__ i __ 0:
				newL = listL[le.(listL) - 1]
			else:
				newL = listL[i - 1]


		# set new layer
		k.sV..(newL)
	

	______

		pass



___ anyListKnob(n, knobName, forwards):

	___

		# get knob
		k = n.knob(knobName)

		# get knob value (int)
		currOp = k.gV..

		# operation count
		countOp = le.(k.values())


		# if forwards scrolling
		__ forwards:

			# if last item in list, go to start
			__ int(currOp) + 1 __ countOp:
				k.sV..(0)

			else:
				# go forward one item
				k.sV..(int(currOp + 1))


		# scroll backwards
		else:

			# if at first item, go to end
			__ currOp __ 0:
				k.sV..(countOp - 1)

			# go back one item
			else:
				k.sV..(int(currOp - 1))

	______

		pass



# make label show knob value (except if in valueMask list)
___ giveLabel(n, knobName):

		# get label knob
		label = n.knob('label')

		# get current label text
		currLabel = label.gV..

		# new label text
		labelText = '[value ' + knobName + ']'


		# check if the label is already present
		__ no. labelText __ currLabel:

			# add original value and new line before new label text if there was a label already, else no new line
			__ currLabel __ '':
				label.sV..(labelText)
			else:
				label.sV..(currLabel + '\n' + labelText)



# cycle node (forwards or backwards)
___ CycleOperations(forwards = True):

	# call function with cycle for each node
	___ i __ ?.sN.. :

		# nodes with custom operation lists
		__ i.C..  __ 'Merge2':
			Merge(i, C_Merge, forwards)
		elif i.C..  __ 'ChannelMerge':
			Merge(i, C_ChannelMerge, forwards)
		elif i.C..  __ 'MergeMat':
			Merge(i, C_MergeMat, forwards)

		# scroll through switch inputs
		elif i.C..  __ 'Switch':
			Switch(i, forwards)

		# swap colorspace in/outs
		elif i.C..  __ 'Colorspace':
			i.knob('swap').execute()
		elif i.C..  __ 'OCIOColorSpace':
			OCIOColorSpace(i)

		# cycle Shuffle
		elif i.C..  __ 'Shuffle':
			Shuffle(i, forwards)

		# cycle Keyer
		elif i.C..  __ 'Keyer':
			anyListKnob(i, 'operation', forwards)

		# up and down FrameHold
		elif i.C..  __ 'FrameHold':
			FrameHold(i, forwards)

		elif i.C..  __ 'Invert':
			anyChannelKnob(i, 'channel', forwards)
		elif i.C..  __ 'Blur':
			anyChannelKnob(i, 'channel', forwards)
		elif i.C..  __ 'Grade':
			anyChannelKnob(i, 'channel', forwards)
		elif i.C..  __ 'Multiply':
			anyChannelKnob(i, 'channel', forwards)
		elif i.C..  __ 'Log2Lin':
			anyListKnob(i, 'operation', forwards)



# autostart (if not imported) - only goes forwards if called this way
__ __name__ __ "__main__":
	CycleOperations()