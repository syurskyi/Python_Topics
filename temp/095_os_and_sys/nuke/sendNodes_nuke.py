# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/3/11

______ os
______ traceback
______ sendNodes_path as SP

inNuke _ SP.inNuke

___
    ______ nuke
except ImportError:
    pass


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
                __ no. os.path.exists(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path))
                for n __ nuke.selectedNodes():
                    nodesName.append(n.knob("name").value())
                __ nodesName !_ []:
                    temp _ " ".join(nodesName)
                    nodesStr _ "%s..." % temp[:30]
                nuke.nodeCopy(path)
            _______
                f _ open("%s/%s/traceback_log.txt" % (SP.USERS_Folder, os.path.expanduser('~').replace('\\','/').split("/")[-1]), 'a')
                traceback.print_exc(file_f)
                f.flush()
                f.close()
                print "send node failed"
    r_ nodesStr


___ clear_selection():
    ___
        for n __ nuke.selectedNodes():
            n.setSelected(False)
    _______
        pass


___ get_nk_name():
    nkName _ ""
    __ inNuke:
        ___
            filePath _ nuke.root().knob("name").value()
            __ filePath == "":
                nkName _ "Untitled"
            else:
                nkName _ filePath.split("/")[-1]
        _______
            print "get nk name failed"
    r_ nkName

