## -----------------------------------------------------------------------------
#   Imports
## -----------------------------------------------------------------------------
______ ___
______ ?

## Load Maya:
___
	______ maya
	_in_maya _ T..
_____ E..
	_in_maya _ F..

## Load Nuke:
___
	______ nuke
	_in_nuke _ T..
_____ E..
	_in_nuke _ F..


## Load Nuke:
___
	______ nuke
	_in_nuke _ T..
_____ E..
	_in_nuke _ F..

## Load Mobu:
___
	______ pyfbsdk
	_in_mobu _ T..
_____ E..
	_in_mobu _ F..

## -----------------------------------------------------------------------------
# Globals
## -----------------------------------------------------------------------------
MSG_FORMAT  _ "%(a_t_)s %(name)s %(l..)s : %(m..)s"
DATE_FORMAT _ "%Y-%m-%d %H:%M:%S"


# Levels - same as logging module
CRITICAL _ 50
FATAL    _ CRITICAL
E.    _ 40
WARNING  _ 30
WARN     _ WARNING
I..     _ 20
D..    _ 10
NOTSET   _ 0



## -----------------------------------------------------------------------------
# getLogger - Main Call
## -----------------------------------------------------------------------------
___ gL..( name, shell_True, maya__in_maya, nuke__in_nuke, mobu__in_mobu, file_None, level_INFO ):
	'''
	Get logger - mimicing the usage of logging.getLogger()
		name(str) : logger name
		shell(bol): output to shell
		maya(bol) : output to maya editor
		nuke(bol) : output to nuke editor
		file(str) : output to given filename
		level(int): logger level
	'''
	r_ Logger( name, shell, maya, nuke, mobu, file, level )



## -----------------------------------------------------------------------------
# Logger Class
## -----------------------------------------------------------------------------
c_ Logger():
	'''
	'''

	___  - (, name, shell_True, maya_False, nuke_False, mobu_False, file_None, level_INFO ):
		'''
		Init Logger
		'''

		__name   _ name
		__logger _ ?.gL..(name)
		__logger.sL..( level )

		## SafetyCheck - Don't create handelr __ logger already have some.
		##               this will prevent double handelrs creation.
		__ __logger.handlers:
			r_

		# Format
		f..  _ ?.F..( MSG_FORMAT, DATE_FORMAT )

		# Shell:
		__ shell:
			stream_hdlr _ ShellHandler()
			stream_hdlr.sF..( f.. )
			__logger.aH..( stream_hdlr )

		# File:
		__ file:
			file_hdlr _ ?.FH..(file)
			file_hdlr.sF..( f.. )
			__logger.aH..( file_hdlr )

		# Maya:
		__ maya and _in_maya:
			maya_hdlr _ MayaHandler()
			maya_hdlr.sF..( f.. )
			__logger.aH..( maya_hdlr )

		# Nuke:
		__ nuke and _in_nuke:
			nuke_hdlr _ NukeHandler()
			nuke_hdlr.sF..( f.. )
			__logger.aH..( nuke_hdlr )

		# Mobu:
		__ mobu and _in_mobu:
			mobu_hdlr _ MobuHandler()
			mobu_hdlr.sF..( f.. )
			__logger.aH..( mobu_hdlr )

	___ __repr__
		'''
		string representation.
		'''
		r_ "%s(%s Level:%i)" % ( __class__, __name, level )

	___ __getattr__(, attr):
		'''
		Use logging.Logger attributes.
		'''
		__ hasattr( __logger, attr ):
			r_ getattr( __logger, attr )
		____
			r_ AttributeError, "No attribute %s" %attr

	## LEVELS
	___ d..(, msg):
		__logger.d..(msg)

	___ i..(, msg):
		__logger.i..(msg)

	___ w..(, msg):
		__logger.w..(msg)

	___ fatal(, msg):
		__logger.fatal(msg)

	___ c..(, msg):
		__logger.c..(msg)


## -----------------------------------------------------------------------------
# ShellHandler
## -----------------------------------------------------------------------------
c_ ShellHandler(?.Handler):
	'''
	Shell Handler - emits logs to shell only.
	by passing maya and nuke editors by using ___.__stdout__
	'''

	___  -
		?.Handler. - ()

	___ emit(, record):

		___
			___.__stdout__.write( "%s\n" %f..(record) )
		_____ IOError:
			## MotionBuilder is doing something funky with python,
			## so sometimes ( not always ) is blocked from writting:
			___.stdout.write( "%s\n" %f..(record) )


## -----------------------------------------------------------------------------
# MayaHandler
## -----------------------------------------------------------------------------
c_ MayaHandler(?.Handler):
	'''
	Maya Handler - emits logs into maya's script editor.
	warning will emit maya.cmds.warning()
	c.. and fatal would popup msg dialog to alert of the error.
	'''
	___  -
		?.Handler. - ()

	___ emit(, record):

		# Formated m..:
		msg _ f..(record)

		__ record.funcName __ "warning":
			maya.cmds.w..( "\n"+msg )

		____ record.funcName __ [ "c..", "fatal" ]:

			## Emit stdout print:
			___.stdout.write("\n"+msg+"\n")

			## Open dialog __ not in batch mode:
			__ maya.cmds.about( batch_True ) __ F..:

				maya.cmds.confirmDialog(title   _ "A %s have accure" %record.funcName,
										m.. _ record.m..,
										button  _ ['Dismiss'],
										messageAlign _ "left")

		____
			___.stdout.write(msg+"\n")


## -----------------------------------------------------------------------------
# NukeHandler
## -----------------------------------------------------------------------------
c_ NukeHandler(?.Handler):
	'''
	Nuke Handler - emits logs into nuke's script editor.
	warning will emit nuke.warning()
	c.. and fatal would popup msg dialog to alert of the error.
	'''
	___  -
		?.Handler. - ()

	___ emit(, record):

		# Formated m..:
		msg _ f..(record)

		__ record.funcName __ "warning":
			nuke.w..(msg)

		____ record.funcName __ [ "c..", "fatal" ]:
			nuke.e..(msg)
			nuke.m..(record.m..)

		____
			___.stdout.write(msg)

## -----------------------------------------------------------------------------
# MobuHandler
## -----------------------------------------------------------------------------
c_ MobuHandler(?.Handler):
	'''
	MotionBuilder Handler - emits logs into motionbuilder's script editor.
	'''
	___  -
		?.Handler. - ()

	___ emit(, record):

		# Formated m..:
		msg _ f..(record)

		__ record.funcName __ "warning":
			___.stdout.write(msg+"\n")

		____ record.funcName __ "error":
			___.s_e...write(msg+"\n")

		____ record.funcName __ [ "c..", "fatal" ]:
			FBMessageBox( record.funcName, msg, "OK" )
			___.s_e...write(msg+"\n")

		____
			___.stdout.write(msg+"\n")


## -----------------------------------------------------------------------------
#  -n
## -----------------------------------------------------------------------------
__  -n __ '__main__':

	log _ gL..( "logger_name", shell_True )
	log.sL..( ?.D.. )
	log.d..('d.. msg')
	log.i..('i.. msg')
	log.w..('warning msg')
	log.fatal('fatal msg')




