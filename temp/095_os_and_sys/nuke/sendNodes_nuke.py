# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/3/11

______ __
______ traceback
______ sendNodes_path __ SP

inNuke _ SP.inNuke

___
    ______ nuke
_____ ImportError:
    p..


___ paste_nk(path):
    __ inNuke:
        ___
            nuke.nodePaste(path)
        _______
            print "paste node failed"


___ send_nk(path):
    nodesName _ []
    nodesStr _ ""
    __ inNuke:
        __ nuke.selectedNodes() !_ []:
            ___
                __ no. __.path.exists(__.path.dirname(path)):
                    __.makedirs(__.path.dirname(path))
                ___ n __ nuke.selectedNodes():
                    nodesName.ap..(n.knob("name").value())
                __ nodesName !_ []:
                    temp _ " ".j..(nodesName)
                    nodesStr _ "%s..." % temp[:30]
                nuke.nodeCopy(path)
            _______
                f _ open("%s/%s/traceback_log.txt" % (SP.USERS_Folder, __.path.expanduser('~').replace('\\','/').split("/")[-1]), 'a')
                traceback.print_exc(file_f)
                f.flush()
                f.close()
                print "send node failed"
    r_ nodesStr


___ clear_selection():
    ___
        ___ n __ nuke.selectedNodes():
            n.setSelected(F..)
    _______
        p..


___ get_nk_name():
    nkName _ ""
    __ inNuke:
        ___
            filePath _ nuke.root().knob("name").value()
            __ filePath __ "":
                nkName _ "Untitled"
            else:
                nkName _ filePath.split("/")[-1]
        _______
            print "get nk name failed"
    r_ nkName

