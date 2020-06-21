# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 6
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ____ g_p_ ______ g_p_
# ____ fabric.api ______ run, env, p.., cd
#
# ___ remote_server
#     e__.h.. _ '127.0.0.1'
#     e__.u.. _ p..'Enter your system username: '
#     e__.p.. _ g_p_('Enter your system user password: ')
#     e__.my.. _ 'localhost'
#     e__.my.. _ p..('Enter your db username: ')
#     e__.my.. _ g_p_('Enter your db user password: ')
#     e__.d_n _ ''
#
# ___ show_dbs
#     """ Wraps mysql show databases cmd"""
#     q _ "show databases"
#     r.. "echo '@' | mysql -u@ -p@" (q, e__.m_u.., e__.my_p..
#
#
# ___ run_sql db_name query
#     """ Generic function to run sql"""
#     w__ c. '/tmp'
#         r.. ("echo '@' | mysql -u@ -p@ -D @" ? e__.m_u.. e__.m_p.. d_n..
#
# ___ create_db
#     """Create a MySQL DB for App version"""
#     __ no. e__.d_n..
#         d_n.. _ p..("Enter the DB name:")
#     ____
#         db_name _ e__.d_n..
#     run('echo "CREATE DATABASE @ default character set utf8 collate utf8_unicode_ci;"|mysql --batch --user=@ --password=@ --host=@'\
#           (d_n.. e__.m_u.. e__.m_p.. e__.m_h.. pty_T..
#
# ___ ls_db
#     """ List a dbs with size in MB """
#     __ no. e__.d_n..
#         db_name _ p..("Which DB to ls?")
#     ____
#         d_n.. _ e__.d_n..
#     query _ """S.. t.._s..                                       "DB Name",
#        Round Su. d.._l.. + i_l..) / 1024 / 1024, 1) "DB Size in MB"
#         F..   i_s_.t..
#         W.. t_s.. = \"@\"
#         G..  B. t_s.. """ d_n..
#     r_s.. d_n.. q..
#
#
# ___ empty_db
#     """ Empty all tables of a given DB """
#     db_name _ p..("Enter DB name to empty:")
#     cmd _ """
#     (echo 'SET foreign_key_checks = 0;';
#     (mysqldump -u@ -p@ --add-drop-table --no-data @ |
#      grep ^DROP);
#      echo 'SET foreign_key_checks = 1;') | \
#      mysql -u@ -p@ -b @
#     """ (e__.m_u.. e__.m_p.. d_n.. e__.m_u_ e__.m_p.. d_n..
#     r.. ?
