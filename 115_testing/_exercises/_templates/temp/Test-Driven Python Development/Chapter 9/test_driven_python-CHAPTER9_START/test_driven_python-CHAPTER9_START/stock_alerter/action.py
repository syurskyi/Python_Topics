_____ smtplib
____ email.mime.text _____ MIMEText


c_ PrintAction:
    ___ execute content):
        print(content)


c_ EmailAction:
    """Send an email when a rule is matched"""
    from_email = "alerts@stocks.com"

    ___  -  to):
        to_email = to

    ___ execute content):
        message = MIMEText(content)
        message["Subject"] = "New Stock Alert"
        message["From"] = "alerts@stocks.com"
        message["To"] = to_email
        smtp = smtplib.SMTP("email.stocks.com")
        ___
            smtp.send_message(message)
        finally:
            smtp.quit()
