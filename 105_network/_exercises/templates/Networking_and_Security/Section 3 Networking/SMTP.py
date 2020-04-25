______ s_l_
____ email.mime.text ______ MIMEText

#  ehlo foo.com
#  mail from:  foo@foo.com
#  rcpt to:  me@me.com
#  data

s _ s_l_.S..("172.30.42.127", 25)
#s.login("user", "password")

___
#  could use the following for a MIME message
#    f = open("myfile", "r")
#    m = MIMEText(f.read())
#    f.close()
#    m['To'] = "kilroy@cloudroy.com"
#    m['From'] = "ricmessier@gmail.com"
#    m['Subject'] = "This is a message to you"

    m _ "\nThis is a message from the last session"
    s.s..mail("ricmessier@gmail.com", "ric@cloudroy.com", m)
    #  send the MIME message
    # s.send_message(m)
    print("Finished sending message")
______ E.. __ e:
    print("Unable to send message: ", e)

s.quit
