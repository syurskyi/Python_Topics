#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ __
______ g_p_
______ re
______ ___
______ smtplib
 
____ e__.mime.image ______ MIMEImage
____ e__.mime.multipart ______ MIMEMultipart
____ e__.mime.text ______ MIMEText
 
SMTP_SERVER _ 'smtp.gmail.com'
SMTP_PORT _ 587
 
___ send_email(sender, recipient):
    """ Send email message """
    msg _ MIMEMultipart()
    msg['Subject'] _ 'Python Emaill Test'
    msg['To'] _ recipient
    msg['From'] _ sender
    subject _ 'Python email Test'
    message _ 'Images attached.'
    # attach imgae files
    files _ __.listdir(__.getcwd())
    gifsearch _ re.compile(".gif", re.IGNORECASE)
    files _ filter(gifsearch.search, files)
    ___ filename __ files:
        pa__ _ __.pa__.j..(__.g_c.., filename)
        __ no. __.pa__.isfile(pa__):
            c..
        img _ MIMEImage(o..(pa__, 'rb').read(), _subtype_"gif")
        img.add_header('Content-Disposition', 'attachment', filename_filename)
        msg.attach(img)
 
    part _ MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    
    # create smtp session
    session _ smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    password _ g_p_.g_p_(prompt_"Enter your Google password: ")
    session.login(sender, password)
    session.sendmail(sender, recipient, msg.as_string())
    print ("Email sent.")
    session.q..
 
__ _______ __ ______
    parser _ ?.AP..(d.._'Email Sending Example')
    parser.a_a..('--sender', a.._"store", d.._"sender")
    parser.a_a..('--recipient', a.._"store", d.._"recipient")
    given_args _ parser.parse_args()
    send_email(given_args.sender, given_args.recipient)
