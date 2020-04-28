#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 6
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

____ getpass ______ getpass
____ fabric.api ______ env, put, sudo, prompt
____ fabric.contrib.files ______ e..

WWW_DOC_ROOT _ "/data/apache/test/"
WWW_USER _ "www-data"
WWW_GROUP _ "www-data"
APACHE_SITES_PATH _ "/etc/apache2/sites-enabled/"
APACHE_INIT_SCRIPT _ "/etc/init.d/apache2 "


___ remote_server
    env.hosts _ ['127.0.0.1']
    env.user _ prompt('Enter user name: ')
    env.password _ getpass('Enter your system password: ')


___ setup_vhost
    """ Setup a test website """
    print ("Preparing the Apache vhost setup...")
    print ("Setting up the document root...")
    __ e..(WWW_DOC_ROOT):
        sudo("rm -rf @" WWW_DOC_ROOT)
    sudo("mkdir -p @" WWW_DOC_ROOT)
    sudo("chown -R @.@ @" (env.user, env.user, WWW_DOC_ROOT))
    put(local_path_"index.html", remote_path_WWW_DOC_ROOT)
    sudo("chown -R @.@ @" (WWW_USER, WWW_GROUP, WWW_DOC_ROOT))
    print ("Setting up the vhost...")
    sudo("chown -R @.@ @" (env.user, env.user, APACHE_SITES_PATH))
    put(local_path_"vhost.conf", remote_path_APACHE_SITES_PATH)
    sudo("chown -R @.@ @" ('root', 'root', APACHE_SITES_PATH))
    sudo("@ restart" APACHE_INIT_SCRIPT)
    print ("Setup complete. Now open the server path http://abc.remote-server.org/ in your web browser.")

