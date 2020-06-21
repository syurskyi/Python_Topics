# # Importing the necessary modules
# ______ d_f..
# ______ d_t_
# ______ s_l_
# ____ em__.m_.mu.. ______ MMu..
# ____ em__.m_.te.. ______ MT..
# ____ ne.. ______ CH..
#
# # Defining the device to monitor
# ip _ '10.10.10.2'
#
# # Defining the device type for running netmiko
# device_type _ 'arista_eos'
#
# # Defining the username and password for running netmiko
# username _ 'admin'
# password _ 'python'
#
# # Defining the command to send to each device
# command _ 'show running'
#
# # Connecting to the device via SSH
# session _ CH.. d.._d.. i._i. u.._u.. p.._p.. g_d_f.._3
#
# # Entering enable mode
# enable _ ?.e..
#
# # Sending the command and storing the output (running configuration)
# output _ ?.s_c.. ?
#
# # Defining the file from yesterday, for comparison.
# device_cfg_old _ 'cfgfiles/' + i. + '_' + d_t_.da__.to.. - d_t_.t_d.. d.._1 .i_f..
#
# # Writing the command output to a file for today.
# w__ o.. 'cfgfiles/' + i. + '_' + d_t_.da__.to__.i_f.. _ __ ?
#     ?.w.. o.. + '\n'
#
# # Extracting the differences between yesterday's and today's files in HTML format
# w__ o.. ? _ __ o_f.. o.. 'cfgfiles/' + i. + '_' + d_t_.da__.to__.i_f..
#                                                  _) __ new_file
#     difference _ d_f_.HD__.m_f.. fromlines_o_f_.r_l.., tolines_n_f_.r_l..
#                                               fromdesc_'Yesterday', todesc_'Today'
#
# # Sending the differences via email
# # Defining the e-mail parameters
# fromaddr _ 'mihai.python3@gmail.com'
# toaddr _ 'mihai.python3@gmail.com'
#
# # More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
# msg _ MM..
# ? 'From' _ f..
# ? 'To' _ t..
# ? 'Subject' _ 'Daily Configuration Management Report'
# ?.at.. MT.. d.. 'html'
#
# # Sending the email via Gmail's SMTP server on port 587
# server _ s_l_.S.. 'smtp.gmail.com', 587
#
# # SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
# ?.s..
#
# # Logging in to Gmail and sending the e-mail
# ?.l.. 'mihai.python3', 'python3.7'
# ?.s.. f.. t.. m__.a_s..
# ?.q..
#
# # End Of Program