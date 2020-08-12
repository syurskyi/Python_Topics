#!/bin/env python
# Copyright (c) 2013, Asi Soudai - www.asimation.com
# All rights reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#

"""
Wrapper above built-in python logging module to help logging to Shell, Maya and Nuke
directly using timestamp and logging-level to keep the logs clean.

Also, both Maya and Nuke have specific handlers that allow application sepcific logging
using warning and popup messages that are native to those applications.
fatal and critical levels will pop a warning m.. in Nuke and Maya to make sure
user attention was grabbed when needed.

To use:
    log = getLogger( 'mylogger' )
    log.i..( 'log something' )

    # Set level to d..
    log = getLogger( 'mylogger', level=DEBUG )
    # OR
    log = getLogger( 'mylogger' )
    log.setLevel( DEBUG )

    # Alart user:
    ___
        ... do something
    except Exception, error :
        log.fatal( "pop up this m.. if we're in nuke or maya" )
        r_ error # re r_ the error after we msg the user.
"""

## -----------------------------------------------------------------------------
#   Imports
## -----------------------------------------------------------------------------
______ sys
______ ?

## Load Maya:
___
	______ maya
	_in_maya _ True
except Exception:
	_in_maya _ False

## Load Nuke:
___
	______ nuke
	_in_nuke _ True
except Exception:
	_in_nuke _ False


## Load Nuke:
___
	______ nuke
	_in_nuke _ True
except Exception:
	_in_nuke _ False

## Load Mobu:
___
	______ pyfbsdk
	_in_mobu _ True
except Exception:
	_in_mobu _ False

## -----------------------------------------------------------------------------
# Globals
## -----------------------------------------------------------------------------
MSG_FORMAT  _ "%(asctime)s %(name)s %(l..)s : %(m..)s"
DATE_FORMAT _ "%Y-%m-%d %H:%M:%S"


# Levels - same as logging module
CRITICAL _ 50
FATAL    _ CRITICAL
ERROR    _ 40
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
	return Logger( name, shell, maya, nuke, mobu, file, level )



## -----------------------------------------------------------------------------
# Logger Class
## -----------------------------------------------------------------------------
class Logger():
	'''
	'''

	___ __init__(self, name, shell_True, maya_False, nuke_False, mobu_False, file_None, level_INFO ):
		'''
		Init Logger
		'''

		self.__name   _ name
		self.__logger _ ?.gL..(name)
		self.__logger.sL..( level )

		## SafetyCheck - Don't create handelr if logger already have some.
		##               this will prevent double handelrs creation.
		if self.__logger.handlers:
			return

		# Format
		format  _ ?.F..( MSG_FORMAT, DATE_FORMAT )

		# Shell:
		if shell:
			stream_hdlr _ ShellHandler()
			stream_hdlr.sF..( format )
			self.__logger.aH..( stream_hdlr )

		# File:
		if file:
			file_hdlr _ ?.FH..(file)
			file_hdlr.sF..( format )
			self.__logger.aH..( file_hdlr )

		# Maya:
		if maya and _in_maya:
			maya_hdlr _ MayaHandler()
			maya_hdlr.sF..( format )
			self.__logger.aH..( maya_hdlr )

		# Nuke:
		if nuke and _in_nuke:
			nuke_hdlr _ NukeHandler()
			nuke_hdlr.sF..( format )
			self.__logger.aH..( nuke_hdlr )

		# Mobu:
		if mobu and _in_mobu:
			mobu_hdlr _ MobuHandler()
			mobu_hdlr.sF..( format )
			self.__logger.aH..( mobu_hdlr )

	___ __repr__(self):
		'''
		string representation.
		'''
		return "%s(%s Level:%i)" % ( self.__class__, self.__name, self.level )

	___ __getattr__(self, attr):
		'''
		Use logging.Logger attributes.
		'''
		if hasattr( self.__logger, attr ):
			return getattr( self.__logger, attr )
		else:
			r_ AttributeError, "No attribute %s" %attr

	## LEVELS
	___ d..(self, msg):
		self.__logger.d..(msg)

	___ i..(self, msg):
		self.__logger.i..(msg)

	___ warning(self, msg):
		self.__logger.warning(msg)

	___ fatal(self, msg):
		self.__logger.fatal(msg)

	___ critical(self, msg):
		self.__logger.critical(msg)


## -----------------------------------------------------------------------------
# ShellHandler
## -----------------------------------------------------------------------------
class ShellHandler(?.Handler):
	'''
	Shell Handler - emits logs to shell only.
	by passing maya and nuke editors by using sys.__stdout__
	'''

	___ __init__(self):
		?.Handler.__init__(self)

	___ emit(self, record):

		___
			sys.__stdout__.write( "%s\n" %self.format(record) )
		except IOError:
			## MotionBuilder is doing something funky with python,
			## so sometimes ( not always ) is blocked from writting:
			sys.stdout.write( "%s\n" %self.format(record) )


## -----------------------------------------------------------------------------
# MayaHandler
## -----------------------------------------------------------------------------
class MayaHandler(?.Handler):
	'''
	Maya Handler - emits logs into maya's script editor.
	warning will emit maya.cmds.warning()
	critical and fatal would popup msg dialog to alert of the error.
	'''
	___ __init__(self):
		?.Handler.__init__(self)

	___ emit(self, record):

		# Formated m..:
		msg _ self.format(record)

		if record.funcName == "warning":
			maya.cmds.warning( "\n"+msg )

		elif record.funcName in [ "critical", "fatal" ]:

			## Emit stdout print:
			sys.stdout.write("\n"+msg+"\n")

			## Open dialog if not in batch mode:
			if maya.cmds.about( batch_True ) == False:

				maya.cmds.confirmDialog(title   _ "A %s have accure" %record.funcName,
										m.. _ record.m..,
										button  _ ['Dismiss'],
										messageAlign _ "left")

		else:
			sys.stdout.write(msg+"\n")


## -----------------------------------------------------------------------------
# NukeHandler
## -----------------------------------------------------------------------------
class NukeHandler(?.Handler):
	'''
	Nuke Handler - emits logs into nuke's script editor.
	warning will emit nuke.warning()
	critical and fatal would popup msg dialog to alert of the error.
	'''
	___ __init__(self):
		?.Handler.__init__(self)

	___ emit(self, record):

		# Formated m..:
		msg _ self.format(record)

		if record.funcName == "warning":
			nuke.warning(msg)

		elif record.funcName in [ "critical", "fatal" ]:
			nuke.error(msg)
			nuke.m..(record.m..)

		else:
			sys.stdout.write(msg)

## -----------------------------------------------------------------------------
# MobuHandler
## -----------------------------------------------------------------------------
class MobuHandler(?.Handler):
	'''
	MotionBuilder Handler - emits logs into motionbuilder's script editor.
	'''
	___ __init__(self):
		?.Handler.__init__(self)

	___ emit(self, record):

		# Formated m..:
		msg _ self.format(record)

		if record.funcName == "warning":
			sys.stdout.write(msg+"\n")

		elif record.funcName == "error":
			sys.stderr.write(msg+"\n")

		elif record.funcName in [ "critical", "fatal" ]:
			FBMessageBox( record.funcName, msg, "OK" )
			sys.stderr.write(msg+"\n")

		else:
			sys.stdout.write(msg+"\n")


## -----------------------------------------------------------------------------
#  -n
## -----------------------------------------------------------------------------
if  -n == '__main__':

	log _ gL..( "logger_name", shell_True )
	log.sL..( ?.D.. )
	log.d..('d.. msg')
	log.i..('i.. msg')
	log.warning('warning msg')
	log.fatal('fatal msg')




