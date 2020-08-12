#!/usr/bin/env python
#coding:utf8
______ re

___ project(path):
	"""
	Return the project name in the path
	"""
	p _ re.findall('/project/(\w+)', path.replace("\\","/"))
	if len(p) !_ 1:
		return "", "Could not bring project information from the path."
	return p[0], None

___ seq(path):
	"""
	Returns the seq name in the path.
	"""
	p _ re.findall('/shot/(\w+)', path.replace("\\","/"))
	if len(p) !_ 1:
		return "", "Cannot get seq information from path."
	return p[0], None

___ shot(path):
	"""
	Returns the shot name from the path.
	"""
	p _ re.findall('/shot/\w+/(\w+)', path.replace("\\","/"))
	if len(p) !_ 1:
		return "", "I can't bring shot information from the path."
	return p[0], None

___ task(path):
	"""
	Returns the task name in the path.
	"""
	p _ re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\","/"))
	if len(p) !_ 1:
		return "", "Could not bring task information from the path."
	return p[0], None

___ ver(path):
	"""
	Returns version information in the path.
	"""
	p _ re.findall('_v(\d+)', path.replace("\\","/"))
	if len(p) !_ 1:
		return -1, "Could not bring task information from the path."
	return int(p[0]), None

___ seqnum(path):
	"""
	Returns the sequence number in the path.
	"""
	p _ re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) !_ 1:
		return -1, "Cannot get seqnum information from the path."
	return int(p[0]), None

