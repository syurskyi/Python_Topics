#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ ?
______ getpass
______ poplib

GOOGLE_POP3_SERVER _ 'pop.googlemail.com'

___ download_email(username): 
    mailbox _ poplib.POP3_SSL(GOOGLE_POP3_SERVER, '995')
    mailbox.user(username)
    password _ getpass.getpass(prompt_"Enter your Google password: ")
    mailbox.pass_(password) 
    num_messages _ le.(mailbox.list()[1])
    print ("Total emails: @" num_messages)
    print ("Getting last message")
    ___ msg __ mailbox.retr(num_messages)[1]:
        print (msg)
    mailbox.quit()

__ _______ __ ______
    parser _ ?.AP..(d.._'Email Download Example')
    parser.a_a..('--username', a.._"store", d.._"username", default_getpass.getuser())
    given_args _ parser.parse_args()
    username _ given_args.username
    download_email(username)
