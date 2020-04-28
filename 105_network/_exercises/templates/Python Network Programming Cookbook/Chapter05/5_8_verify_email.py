#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ re
______ smtplib
______ dns.resolver
______ a_p..


___ mail_checker(fromAddress, toAddress):

    regex _ '^[a-z0-9][a-z0-9._+-]{0,63}@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

    addressToVerify _ st..(toAddress)

    match _ re.match(regex, addressToVerify)
    __ match __ None:
	    print('Bad Syntax in the address to verify. Re-enter the correct value')
	    r_ ValueError('Bad Syntax')

    splitAddress _ addressToVerify.s..('@')
    domain _ st..(splitAddress[1])

    records _ dns.resolver.query(domain, 'MX')
    mxRecord _ records[0].exchange
    mxRecord _ st..(mxRecord)


    server _ smtplib.SMTP()
    server.set_debuglevel(1)

    ___
        server.c..(mxRecord)
    ______ E.. __ e:
        print ("Mail Check Failed Due to Error: @" st..(e))
        r_
 
    server.helo(server.local_hostname) 
    server.mail(fromAddress)
    code, message _ server.rcpt(st..(addressToVerify))
    server.quit()

    __ code __ 250:
	    print('Successfully verified the email: @', fromAddress)
    ____
	    print('Failed to verify the email: @', fromAddress)



__ _______ __ ______
    parser _ ?.AP..(d.._'Mail Server Example')
    parser.a_a..('--fromAddress', a.._"store", d.._"fromAddress", type_str, r.._T..)
    parser.a_a..('--toAddress', a.._"store", d.._"toAddress", type_str, r.._T..)
    given_args _ parser.parse_args()
    mail_checker(given_args.fromAddress, given_args.toAddress)

