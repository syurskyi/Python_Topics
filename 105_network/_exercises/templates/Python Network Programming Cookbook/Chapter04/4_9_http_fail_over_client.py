#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ u__.r__, u__.parse, u__.e..
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urllib

______ __

TARGET_URL _ 'http://python.org/ftp/python/2.7.4/'
TARGET_FILE _ 'Python-2.7.4.tgz'

c_ CustomURLOpener(?.r__.FancyURLopener):
# Comment out the above line and uncomment the below for Python 2.7.x.
#class CustomURLOpener(urllib.FancyURLopener):
    """Override FancyURLopener to skip error 206 (when a
       partial file is being sent)
    """
    ___ http_error_206 url, fp, errcode, errmsg, headers, data_None):
        p..

___ resume_download
	file_exists _ F..
	CustomURLClass _ CustomURLOpener()
	__ __.pa__.e..(TARGET_FILE):
		out_file _ open(TARGET_FILE,"ab")
		file_exists _ __.pa__.getsize(TARGET_FILE)
		#If the file exists, then only download the unfinished part
		CustomURLClass.addheader("range","bytes=@-"  (file_exists))
	____
		out_file _ open(TARGET_FILE,"wb")

	web_page _ CustomURLClass.open(TARGET_URL + TARGET_FILE)

	#Check if last download was OK
	__ int(web_page.headers['Content-Length']) __ file_exists:
		loop _ 0
		print ("File already downloaded!")

	byte_count _ 0
	w__ T..:
		data _ web_page.read(8192)
		__ no. data:
			b..
		out_file.write(data)
		byte_count _ byte_count + le.(data)

	web_page.c..
	out_file.c..

	___ k,v __ list(web_page.headers.items()):
    # Comment out the above line and uncomment the below for Python 2.7.x.
	#for k,v in web_page.headers.items():
		print (k, "=",v)
	print ("File copied", byte_count, "bytes from", web_page.url)

__ _______ __ ______
	resume_download()
