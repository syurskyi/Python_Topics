#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ __
______ a_p..
______ smtplib
______ zipfile
______ tempfile
____ email ______ encoders
____ email.mime.base ______ MIMEBase
____ email.mime.multipart ______ MIMEMultipart

___ email_dir_zipped(sender, recipient):
    zf _ tempfile.TemporaryFile(prefix_'mail', suffix_'.zip')
    zip _ zipfile.ZipFile(zf, 'w')
    print ("Zipping current dir: @" __.getcwd())
    ___ file_name __ __.listdir(__.getcwd()):
        zip.write(file_name)
    zip.c..
    zf.seek(0)

    # Create the message
    print ("Creating email message...")
    email_msg _ MIMEMultipart()
    email_msg['Subject'] _ 'File from path @' __.getcwd()
    email_msg['To'] _ ', '.j..(recipient)
    email_msg['From'] _ sender
    email_msg.preamble _ 'Testing email from Python.\n'
    msg _ MIMEBase('application', 'zip')
    msg.set_payload(zf.read())
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', 
                   filename_os.getcwd()[-1] + '.zip')
    email_msg.attach(msg)
    email_msg _ email_msg.as_string()

    # send the message
    print ("Sending email message...")
    ___
        smtp _ smtplib.SMTP('localhost')
        smtp.set_debuglevel(1)
        smtp.sendmail(sender, recipient, email_msg)
    ______ E.. __ e:
        print ("Error: @" st..(e))
    f..
        smtp.c..

__ _______ __ ______
    parser _ ?.AP..(d.._'Email Example')
    ?.a_a..('--sender', a.._"store", d.._"sender", default_'you@you.com')
    ?.a_a..('--recipient', a.._"store", d.._"recipient")
    given_args _ ?.parse_args()
    email_dir_zipped(?.sender, ?.recipient)
