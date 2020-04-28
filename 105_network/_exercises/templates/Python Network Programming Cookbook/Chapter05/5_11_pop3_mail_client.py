#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ getpass
______ poplib
______ a_p..

___ mail_client(host, port, user, password):
    Mailbox _ poplib.POP3_SSL(host, port) 
    Mailbox.user(user) 
    Mailbox.pass_(password) 
    numMessages _ le.(Mailbox.list()[1])
    print (Mailbox.retr(1)[1])
    Mailbox.quit()


__ _______ __ ______
    parser _ ?.AP..(d.._'Mail Server Example')
    parser.a_a..('--host', a.._"store", d.._"host", type_str, r.._T..)
    parser.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    parser.a_a..('--user', a.._"store", d.._"user", type_str, r.._T..)
    password _ getpass.getpass("Enter your Password:")
    given_args _ parser.parse_args()
    mail_client(?.host, ?.port, ?.user, password)

