#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ g_p_
______ imaplib

GOOGLE_IMAP_SERVER _ 'imap.googlemail.com'

___ check_email(username): 
    mailbox _ imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, '993') 
    password _ g_p_.g_p_(prompt_"Enter your Google password: ")
    mailbox.login(username, password)
    mailbox.se__('Inbox')
    typ, data _ mailbox.search(N.., 'ALL')
    ___ num __ data[0].s..
        typ, data _ mailbox.fetch(num, '(RFC822)')
        print ('Message @\n@\n'  (num, data[0][1]))
        b..
    mailbox.c..
    mailbox.logout()
    

__ _______ __ ______
    parser _ ?.AP..(d.._'Email Download Example')
    ?.a_a..('--username', a.._"store", d.._"username", d.._getpass.g_u_
    given_args _ ?.p_a..
    username _ ?.username
    check_email(username)
