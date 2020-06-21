# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 6
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ____ g_p_ ______ g_p_
# ____ f__.api ______ env  put  sudo  p..
# ____ f__.contrib.files ______ e..
#
# WWW_DOC_ROOT _ "/data/apache/test/"
# WWW_USER _ "www-data"
# WWW_GROUP _ "www-data"
# APACHE_SITES_PATH _ "/etc/apache2/sites-enabled/"
# APACHE_INIT_SCRIPT _ "/etc/init.d/apache2 "
#
#
# ___ remote_server
#     e__.h.. _ '127.0.0.1'
#     e__.u.. _ p..('Enter user name: ')
#     e__.p.. _ g_p_('Enter your system password: ')
#
#
# ___ setup_vhost
#     """ Setup a test website """
#     print ("Preparing the Apache vhost setup...")
#     print ("Setting up the document root...")
#     __ e..?_D..
#         su.. "rm -rf @" _D..
#     ? "mkdir -p @" _D..
#     ? "chown -R @.@ @" e__.u.. e__.u.. _D..
#     p.. l_p_"index.html" r_p..__D..
#     ? "chown -R @.@ @" _U  _G _D
#     print ("Setting up the vhost...")
#     ? "chown -R @.@ @" e__.u.. e__.u..  A..
#     p.. l_p.._"vhost.conf"  r.._A..
#     ? "chown -R @.@ @" ('root'  'root'  A..
#     ? "@ restart" A_I..
#     print ("Setup complete. Now open the server path http://abc.remote-server.org/ in your web browser.")
#
