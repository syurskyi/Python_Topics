#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ http.cookiejar 
# Comment out the above line and uncomment the below for Python 2.7.x.
#import cookielib 

______ u__

# Uncomment the below line for Python 2.7.x.
#import urllib2


ID_USERNAME _ 'id_username'
ID_PASSWORD _ 'id_password'
USERNAME _ 'you@email.com'
PASSWORD _ 'mypassword'
LOGIN_URL _ 'https://bitbucket.org/account/signin/?next=/'
NORMAL_URL _ 'https://bitbucket.org/'

___ extract_cookie_info
    """ Fake login to a site with cookie"""
    # setup cookie jar

    cj _ http.cookiejar.CookieJar()
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #cj = cookielib.CookieJar()

    login_data _ ?.parse.urlencode({ID_USERNAME : USERNAME, ID_PASSWORD : PASSWORD}).e..("utf-8")
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #login_data = urllib.urlencode({ID_USERNAME : USERNAME, ID_PASSWORD : PASSWORD})

    # create url opener

    opener _ ?.r__.build_opener(?.r__.HTTPCookieProcessor(cj))
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    resp _ opener.open(LOGIN_URL, login_data)

    # send login info 
    ___ cookie __ cj:
        print ("----First time cookie: @ --> @" (cookie.name, cookie.value))
    print ("Headers: @" resp.headers)

    # now access without any login info
    resp _ opener.open(NORMAL_URL)
    ___ cookie __ cj:
        print ("++++Second time cookie: @ --> @" (cookie.name, cookie.value))
    
    print ("Headers: @" resp.headers)

__ _______ __ ______
    extract_cookie_info()
