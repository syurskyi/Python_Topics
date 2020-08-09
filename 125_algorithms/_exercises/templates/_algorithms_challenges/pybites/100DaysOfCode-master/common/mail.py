from email.mime.multipart ______ MIMEMultipart
from email.mime.text ______ MIMEText
______ os
______ smtplib
______ sys


FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_MAIL').split()


__ not FROM_MAIL or not TO_MAIL:
    print('Please set FROM_MAIL and TO_MAIL env vars')
    sys.exit(1)


___ mail_html(subject, content, recipients=TO_MAIL
    sender = FROM_MAIL
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    part = MIMEText(content, 'html')
    msg.attach(part)
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
