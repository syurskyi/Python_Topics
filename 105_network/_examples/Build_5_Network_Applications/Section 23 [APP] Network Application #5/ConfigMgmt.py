# Importing the necessary modules
import difflib
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler

# Defining the device to monitor
ip = '10.10.10.2'

# Defining the device type for running netmiko
device_type = 'arista_eos'

# Defining the username and password for running netmiko
username = 'admin'
password = 'python'

# Defining the command to send to each device
command = 'show running'

# Connecting to the device via SSH
session = ConnectHandler(device_type=device_type, ip=ip, username=username, password=password, global_delay_factor=3)

# Entering enable mode
enable = session.enable()

# Sending the command and storing the output (running configuration)
output = session.send_command(command)

# Defining the file from yesterday, for comparison.
device_cfg_old = 'cfgfiles/' + ip + '_' + (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

# Writing the command output to a file for today.
with open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')

# Extracting the differences between yesterday's and today's files in HTML format
with open(device_cfg_old, 'r') as old_file, open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(),
                                                 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines=old_file.readlines(), tolines=new_file.readlines(),
                                              fromdesc='Yesterday', todesc='Today')

# Sending the differences via email
# Defining the e-mail parameters
fromaddr = 'mihai.python3@gmail.com'
toaddr = 'mihai.python3@gmail.com'

# More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Daily Configuration Management Report'
msg.attach(MIMEText(difference, 'html'))

# Sending the email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)

# SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
server.starttls()

# Logging in to Gmail and sending the e-mail
server.login('mihai.python3', 'python3.7')
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()

# End Of Program