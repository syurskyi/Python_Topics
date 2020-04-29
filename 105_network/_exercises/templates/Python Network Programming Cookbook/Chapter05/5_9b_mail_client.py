#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ smtplib
______ e__.utils
______ a_p..
____ e__.mime.text ______ MIMEText

___ mail_client(host, port, fromAddress, toAddress, subject, body):
    msg _ MIMEText(body)
    msg['To'] _ e__.utils.formataddr(('Recipient', toAddress))
    msg['From'] _ e__.utils.formataddr(('Author', fromAddress))
    msg['Subject'] _ subject

    server _ smtplib.SMTP(host, port)
    s...set_debuglevel(T..)
    ___
        s...sendmail(fromAddress, toAddress, msg.as_string())
    f..
        s...q..


__ _______ __ ______
    parser _ ?.AP..(d.._'Mail Server Example')
    ?.a_a..('--host', a.._"store", d.._"host", type_str, r.._T..)
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    ?.a_a..('--fromAddress', a.._"store", d.._"fromAddress", type_str, r.._T..)
    ?.a_a..('--toAddress', a.._"store", d.._"toAddress", type_str, r.._T..)
    ?.a_a..('--subject', a.._"store", d.._"subject", type_str, r.._T..)
    ?.a_a..('--body', a.._"store", d.._"body", type_str, r.._T..)
    given_args _ ?.p_a..
    mail_client(?.host, ?.port, ?.fromAddress, ?.toAddress, ?.subject, ?.body)

