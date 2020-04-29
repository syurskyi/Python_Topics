#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 6
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


____ g_p_ ______ g_p_
____ fabric.api ______ local, run, env, get, put, prompt, open_shell

___ remote_server
    env.hosts _ ['127.0.0.1']
    env.password _ g_p_('Enter your system password: ')
    env.home_folder _ '/tmp'

___ login
    open_shell(command_"cd @" env.home_folder)


___ download_file
    print ("Checking local disk space...")
    local("df -h")
    remote_path _ prompt("Enter the remote file path:")
    local_path _ prompt("Enter the local file path:")
    get(remote_path_remote_path, local_path_local_path)
    local("ls @" local_path)


___ upload_file
    print ("Checking remote disk space...")
    run("df -h")
    local_path _ prompt("Enter the local file path:")
    remote_path _ prompt("Enter the remote file path:")
    put(remote_path_remote_path, local_path_local_path)
    run("ls @" remote_path)


