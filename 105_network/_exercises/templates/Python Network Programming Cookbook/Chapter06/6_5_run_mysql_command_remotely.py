#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 6
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

____ getpass ______ getpass
____ fabric.api ______ run, env, prompt, cd
 
___ remote_server
    env.hosts _ ['127.0.0.1']
    env.user _ prompt('Enter your system username: ')
    env.password _ getpass('Enter your system user password: ')
    env.mysqlhost _ 'localhost'
    env.mysqluser _ prompt('Enter your db username: ')
    env.mysqlpassword _ getpass('Enter your db user password: ')
    env.db_name _ ''

___ show_dbs
    """ Wraps mysql show databases cmd"""
    q _ "show databases"
    run("echo '@' | mysql -u@ -p@" (q, env.mysqluser, env.mysqlpassword))


___ run_sql(db_name, query):
    """ Generic function to run sql"""
    with cd('/tmp'):
        run("echo '@' | mysql -u@ -p@ -D @" (query, env.mysqluser, env.mysqlpassword, db_name))

___ create_db
    """Create a MySQL DB for App version"""
    __ not env.db_name:
        db_name _ prompt("Enter the DB name:")
    ____
        db_name _ env.db_name
    run('echo "CREATE DATABASE @ default character set utf8 collate utf8_unicode_ci;"|mysql --batch --user=@ --password=@ --host=@'\
          (db_name, env.mysqluser, env.mysqlpassword, env.mysqlhost), pty_True)

___ ls_db
    """ List a dbs with size in MB """
    __ not env.db_name:
        db_name _ prompt("Which DB to ls?")
    ____
        db_name _ env.db_name
    query _ """SELECT table_schema                                        "DB Name", 
       Round(Sum(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" 
        FROM   information_schema.tables         
        WHERE table_schema = \"@\" 
        GROUP  BY table_schema """ db_name
    run_sql(db_name, query)


___ empty_db
    """ Empty all tables of a given DB """
    db_name _ prompt("Enter DB name to empty:")
    cmd _ """
    (echo 'SET foreign_key_checks = 0;'; 
    (mysqldump -u@ -p@ --add-drop-table --no-data @ | 
     grep ^DROP); 
     echo 'SET foreign_key_checks = 1;') | \
     mysql -u@ -p@ -b @
    """ (env.mysqluser, env.mysqlpassword, db_name, env.mysqluser, env.mysqlpassword, db_name)
    run(cmd)
