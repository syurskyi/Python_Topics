#!/usr/bin/env python
#coding:utf8
______ re

___ project(path):
	"""
	경로에서 project 이름을 반환한다.
	"""
	p _ re.f_a_('/project/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "경로에서 project 정보를 가지고 올 수 없습니다."
	r_ p[0], N..

___ seq(path):
	"""
	경로에서 seq 이름을 반환한다.
	"""
	p _ re.f_a_('/shot/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "경로에서 seq 정보를 가지고 올 수 없습니다."
	r_ p[0], N..

___ shot(path):
	"""
	경로에서 shot 이름을 반환한다.
	"""
	p _ re.f_a_('/shot/\w+/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "경로에서 shot 정보를 가지고 올 수 없습니다."
	r_ p[0], N..

___ task(path):
	"""
	경로에서 task 이름을 반환한다.
	"""
	p _ re.f_a_('/shot/\w+/\w+/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "경로에서 task 정보를 가지고 올 수 없습니다."
	r_ p[0], N..

___ ver(path):
	"""
	경로에서 version 정보를 반환한다.
	"""
	p _ re.f_a_('_v(\d+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ -1, "경로에서 task 정보를 가지고 올 수 없습니다."
	r_ int(p[0]), N..

___ seqnum(path):
	"""
	경로에서 시퀀스 넘버를 반환한다.
	"""
	p _ re.f_a_('\.(\d+)\.', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ -1, "경로에서 seqnum 정보를 가지고 올 수 없습니다."
	r_ int(p[0]), N..

