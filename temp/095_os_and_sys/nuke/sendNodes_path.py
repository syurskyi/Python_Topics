# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/3/7

______ os
______ sys

inNuke _ False

try:
    ______ nuke
    inNuke _ True
except:
    print "not in nuke"

ThisPath _ __file__


USERS_Folder _ "C:/Temp/SendNodes_users"
GLOBAL_Folder _ os.path.dirname(ThisPath)









