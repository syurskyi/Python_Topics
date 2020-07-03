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
______ helper
______ init

g__ default_dir
g__ knobInit
g__ ctrl

default_dir = __.path.dirname(__file__)
knobInit = default_dir+"/init.py"
ctrl = False


___ checkExistingInit():
	'''
	check if knobInit exists
	if not create one
	'''
	
	__ no. __.path.isfile(knobInit):
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

___ createDefault():
	'''
	create custom knobDefault value
	'''

	n = ?.thisNode()
	k = ?.thisKnob()
	
	#set default for current nuke session
	?.knobDefault("{node}.{knob}".format(node=n.Class(), knob=k.name()), "{val}".format(val=k.value()))

	# set 
	updateKnobInit(n.Class(),k.name(),k.v..,"write")

___ resetToDefault():
	'''
	reset to standard knob default value
	'''

	n = ?.thisNode()
	k = ?.thisKnob()

	k.sV..(k.defaultValue())
	?.knobDefault("{node}.{knob}".format(node=n.Class(), knob=k.name()), "{val}".format(val=k.defaultValue()))
	updateKnobInit(n.Class(),k.name(),"","del")

___ updateKnobInit(node,knob,value,mode):
	'''
	update knob init.py - delete or append knobDefault depending on mode
	'''

	knobDefaults = helper.openFileReturnArr(knobInit)

	__ mode __ "del":
		
		found = 0

		___ d __ knobDefaults:
			__ "{node}.{knob}".format(node=node, knob=knob) __ d:
				found+=1
				__ ctrl __ T..:
					print "found in knobInit"
					print d
				knobDefaults.remove(d)
			____
				pass
		__ found < 1:
			__ ctrl __ T..:
				print "not found in knobInit"
		
		#write new knobInit
		___
			f = o..(knobInit,'w+')
			___ d __ knobDefaults:
				f.write(d+"\n")
			f.c__
		______
			?.m..("an error occured while trying to edit the knobDefaults file")

	__ mode __ "write":
		#get rid of old knobDefaults of the current knob and write new knobDefault			
		updateKnobInit(node,knob,"","del")
		___
			f = o..(knobInit,'a')
			newKnobDefault = 'nuke.knobDefault("{node}.{knob}", "{val}")\n'.format(node=node, knob=knob, val=value)
			f.write(newKnobDefault)
			f.c__
		______
			?.m..("an error occured while trying to edit the knobDefaults file")

checkExistingInit()





