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


C_Merge _ []
C_ChannelMerge _ []
C_MergeMat _ []



#########################################


# TODO fix cycleoperations is other way around with valuemask, check blur or grade



_____ ?




___ Merge(n, cycle, forwards):

	___

		# get knob
		k _ n.knob('operation')


		# if custom list is used
		__ le.(cycle) > 0:

			# get knob value as str
			currOp _ k.v.. ()

			# check if current value is in cycle
			nextOp _ ''

			__ currOp __ cycle:

				# get next or pevious item index (depending on forwards)
				index _ cycle.index(currOp) + (1 __ forwards else -1)

				# return to 0 if out of range
				__(index > (le.(cycle)) - 1):
					index _ 0

				# set new value
				nextOp _ cycle[index]
			____

				# reset to first in cycle
				nextOp _ cycle[0]

			# set new value to knob
			n.knob("operation").sV..(nextOp)


		# if not, simply scroll through all options
		____

			# current operation
			currOp _ k.gV..

			# operation count
			countOp _ le.(k.values())

			__ forwards:

				# if last item in list, go to start
				__ in_(currOp) + 1 __ countOp:
					k.sV..(0)

				____
					k.sV..(in_(currOp) + 1)

			____

				__ currOp __ 0:
					k.sV..(countOp - 1)
				____
					k.sV..(in_(currOp) - 1)

	______

		pass



___ Switch(n, forwards):

	___

		# get current value
		currWhich _ n.knob('which').gV..
		# get amount of inputs on Switch (-1, to match input index which starts counting at 0)
		maxWhich _ n.inputs() - 1.0

		# make Switch nodes with only one input alternate between 1 and 0
		__(maxWhich __ 0):
			maxWhich _ 1

		# new value for Which on Switch
		newWhich _ -1.0
		__ forwards:

			newWhich _ currWhich + 1.0
			__ maxWhich < newWhich:
				newWhich _ 0.0

		____

			newWhich _ currWhich - 1.0
			__ newWhich < 0.0:
				newWhich _ maxWhich

		n.knob('which').sV..(newWhich)

	______

		pass



___ OCIOColorSpace(n):

	___

		# get knobs
		k1 _ n.knob('in_colorspace')
		k2 _ n.knob('out_colorspace')

		# get values
		inC _ k1.v.. ()
		outC _ k2.v.. ()

		# set inverse values
		k1.sV..(outC)
		k2.sV..(inC)

	______

		pass



___ Shuffle(n, forwards):

	___

		# get knob
		k _ n.knob('in')

		# get current layer (str)
		currL _ k.v.. ()

		# get all existing layers
		listL _ ?.layers()

		# get index of current layer
		i _ 0
		___ eachL __ listL:
			__ eachL __ currL:
				break
			i +_ 1

		# get new layer
		__ forwards:

			__ le.(listL) __ i + 1:
				newL _ listL[0]
			____
				newL _ listL[i + 1]

		____

			__ i __ 0:
				newL _ listL[le.(listL) - 1]
			____
				newL _ listL[i - 1]


		# set new layer
		k.sV..(newL)


		# set label
		giveLabel(n, 'in')

	______

		pass



___ FrameHold(n, forwards):

	___

		# get knob
		k _ n.knob('first_frame')

		# get current frame
		currF _ k.gV..

		# next value
		newF _ currF + 1 __ forwards else currF - 1

		# set new value
		k.sV..(newF)

	______

		pass



___ anyChannelKnob(n, knobName, forwards):

	___

		# get knob
		k _ n.knob(knobName)

		# get knob value (str)
		currL _ k.v.. ()

		# get all possible layers
		listL _ ?.layers()
		listL.insert(0, 'all')
		listL.insert(1, 'none')

		# get index of current layer
		i _ 0
		___ eachL __ listL:
			__ eachL __ currL:
				break
			i +_ 1



		# get new layer
		__ forwards:

			__ le.(listL) __ i + 1:
				newL _ listL[0]
			____
				newL _ listL[i + 1]

		____

			__ i __ 0:
				newL _ listL[le.(listL) - 1]
			____
				newL _ listL[i - 1]


		# set new layer
		k.sV..(newL)
	

	______

		pass



___ anyListKnob(n, knobName, forwards):

	___

		# get knob
		k _ n.knob(knobName)

		# get knob value (int)
		currOp _ k.gV..

		# operation count
		countOp _ le.(k.values())


		# if forwards scrolling
		__ forwards:

			# if last item in list, go to start
			__ in_(currOp) + 1 __ countOp:
				k.sV..(0)

			____
				# go forward one item
				k.sV..(in_(currOp + 1))


		# scroll backwards
		____

			# if at first item, go to end
			__ currOp __ 0:
				k.sV..(countOp - 1)

			# go back one item
			____
				k.sV..(in_(currOp - 1))

	______

		pass



# make label show knob value (except if in valueMask list)
___ giveLabel(n, knobName):

		# get label knob
		label _ n.knob('label')

		# get current label text
		currLabel _ label.gV..

		# new label text
		labelText _ '[value ' + knobName + ']'


		# check if the label is already present
		__ no. labelText __ currLabel:

			# add original value and new line before new label text if there was a label already, else no new line
			__ currLabel __ '':
				label.sV..(labelText)
			____
				label.sV..(currLabel + '\n' + labelText)



# cycle node (forwards or backwards)
___ CycleOperations(forwards _ T..):

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