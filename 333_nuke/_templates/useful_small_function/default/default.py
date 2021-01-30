###########################################################################################################
#
#  default
#  
#  @author simon jokuschies
#  @version 1.0
#  @contact info@leafpictures.de
#  @website www.leafpictures.de
#
#  description:
#  Set knob defaults on the fly so you dont't have to write them manually into your nuke home directory.
#  Just set a knob like you want to have it as knobdefault and then right click, choose myDefaults - set as knob default
#  If you want to get rid of the knob default just right click on the knob and choose myDefaults - reset.
#
#  instalation
#
#  put myDefaults folder inside nuke home directory. In your int.py write (without the '#'):
#  nuke.pluginAddPath("default")
#
##########################################################################################################

#no need to change anything from here. Edit only if you exactly know what you're doing.

______ ?
______ __
______ h__
______ init

g__ default_dir
g__ knobInit
g__ ctrl

default_dir _ __.pa__.d_n_( -f)
knobInit _ default_dir+"/init.py"
ctrl _ F..


___ checkExistingInit
	'''
	check if knobInit exists
	if not create one
	'''
	
	__ no. __.pa__.isf..(knobInit):
		___
			o..(knobInit,'w')
			__ ctrl __ T..:
					print "created knobInit"
		______
			__ ctrl __ T..:
					print "couldn't create knobInit"
	____
		__ ctrl __ T..:
			print "knobInit exists"

___ createDefault
	'''
	create custom knobDefault value
	'''

	n _ ?.tN..()
	k _ ?.tK..
	
	#set default for current nuke session
	?.knobDefault("{node}.{knob}".f..(node_n.Class(), knob_k.n.., "{val}".f..(val_k.v.. ()))

	# set 
	updateKnobInit(n.Class(),k.n.. ,k.v..,"write")

___ resetToDefault
	'''
	reset to standard knob default value
	'''

	n _ ?.tN..()
	k _ ?.tK..

	k.sV..(k.defaultValue())
	?.knobDefault("{node}.{knob}".f..(node_n.Class(), knob_k.n.., "{val}".f..(val_k.defaultValue()))
	updateKnobInit(n.Class(),k.n.. ,"","del")

___ updateKnobInit(node,knob,v.. ,mode):
	'''
	update knob init.py - delete or append knobDefault depending on mode
	'''

	knobDefaults _ h__.openFileReturnArr(knobInit)

	__ mode __ "del":
		
		found _ 0

		___ d __ knobDefaults:
			__ "{node}.{knob}".f..(node_node, knob_knob) __ d:
				found+_1
				__ ctrl __ T..:
					print "found in knobInit"
					print d
				knobDefaults.r__(d)
			____
				p..
		__ found < 1:
			__ ctrl __ T..:
				print "not found in knobInit"
		
		#write new knobInit
		___
			f _ o..(knobInit,'w+')
			___ d __ knobDefaults:
				f.w..(d+"\n")
			f.c__
		______
			?.m..("an error occured while trying to edit the knobDefaults file")

	__ mode __ "write":
		#get rid of old knobDefaults of the current knob and write new knobDefault			
		updateKnobInit(node,knob,"","del")
		___
			f _ o..(knobInit,'a')
			newKnobDefault _ 'nuke.knobDefault("{node}.{knob}", "{val}")\n'.f..(node_node, knob_knob, val_value)
			f.w..(newKnobDefault)
			f.c__
		______
			?.m..("an error occured while trying to edit the knobDefaults file")

checkExistingInit()





