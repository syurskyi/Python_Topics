# Importing the necessary modules
______ difflib
______ d_t_
______ s_l_
____ email.mime.multipart ______ MIMEMultipart
____ email.mime.text ______ MIMEText
____ netmiko ______ ConnectHandler

# Defining the device to monitor
ip _ '10.10.10.2'

# Defining the device type for running netmiko
device_type _ 'arista_eos'

# Defining the username and password for running netmiko
username _ 'admin'
p__swor. _ 'python'

# Defining the command to send to each device
command _ 'show running'

# Connecting to the device via SSH
session _ ConnectHandler(device_type_device_type, ip_ip, username_username, p__swor._p__swor., global_delay_factor_3)

# Entering enable mode
enable _ session.enable

# Sending the command and storing the output (running configuration)
output _ session.s.._command(command)

# Defining the file from yesterday, for comparison.
device_cfg_old _ 'cfgfiles/' + ip + '_' + (d_t_.date.today - d_t_.timedelta(days_1)).isoformat

# Writing the command output to a file for today.
w__ o..('cfgfiles/' + ip + '_' + d_t_.date.today.isoformat, 'w') __ device_cfg_new:
    device_cfg_new.w..(output + '\n')

# Extracting the differences between yesterday's and today's files in HTML format
w__ o..(device_cfg_old, _) __ old_file, o..('cfgfiles/' + ip + '_' + d_t_.date.today.isoformat,
                                                 _) __ new_file:
    difference _ difflib.HtmlDiff.make_file(____lines_old_file.r_l.., tolines_new_file.r_l..,
                                              ____desc_'Yesterday', todesc_'Today')

# Sending the differences via email
# Defining the e-mail parameters
____addr _ 'mihai.python3@gmail.com'
toaddr _ 'mihai.python3@gmail.com'

# More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
msg _ MIMEMultipart
msg['From'] _ ____addr
msg['To'] _ toaddr
msg['Subject'] _ 'Daily Configuration Management Report'
msg.attach(MIMEText(difference, 'html'))

# Sending the email via Gmail's SMTP server on port 587
server _ s_l_.S..('smtp.gmail.com', 587)

# SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
server.starttls

# Logging in to Gmail and sending the e-mail
server.l..('mihai.python3', 'python3.7')
server.s..mail(____addr, toaddr, msg.___string)
server.quit

# End Of Program