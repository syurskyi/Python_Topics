#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ smtplib
____ e__.mime.multipart ______ MIMEMultipart
____ e__.mime.text ______ MIMEText
______ a_p..
______ g_p_

___ mail_client(host, port, fromAddress, password, toAddress, subject, body):
    msg _ MIMEMultipart()

    msg['From'] _ fromAddress
    msg['To'] _ toAddress
    msg['Subject'] _ subject
    message _ body
    msg.attach(MIMEText(message))

    mailserver _ smtplib.SMTP(host,port)

    # Identify to the SMTP Gmail Client
    mailserver.ehlo()

    # Secure with TLS Encryption
    mailserver.starttls()

    # Reidentifying as an encrypted connection
    mailserver.ehlo()
    mailserver.login(fromAddress, password)

    mailserver.sendmail(fromAddress,toAddress,msg.as_string())
    print ("Email sent from:", fromAddress)

    mailserver.q..



__ _______ __ ______
    parser _ ?.AP..(d.._'Mail Server Example')
    parser.a_a..('--host', a.._"store", d.._"host", type_str, r.._T..)
    parser.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    parser.a_a..('--fromAddress', a.._"store", d.._"fromAddress", type_str, r.._T..)
    parser.a_a..('--toAddress', a.._"store", d.._"toAddress", type_str, r.._T..)
    parser.a_a..('--subject', a.._"store", d.._"subject", type_str, r.._T..)
    parser.a_a..('--body', a.._"store", d.._"body", type_str, r.._T..)
    password _ g_p_.g_p_("Enter your Password:")
    given_args _ parser.parse_args()
    mail_client(?.host, given_args.port, given_args.fromAddress, password, given_args.toAddress, given_args.subject, given_args.body)

