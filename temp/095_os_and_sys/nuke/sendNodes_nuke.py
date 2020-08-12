# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/3/11

______ os
______ traceback
______ sendNodes_path as SP

inNuke _ SP.inNuke

try:
    ______ nuke
except ImportError:
    pass


def paste_nk(path):
    if inNuke:
        try:
            nuke.nodePaste(path)
        except:
            print "paste node failed"


def send_nk(path):
    nodesName _ []
    nodesStr _ ""
    if inNuke:
        if nuke.selectedNodes() !_ []:
            try:
                if not os.path.exists(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path))
                for n in nuke.selectedNodes():
                    nodesName.append(n.knob("name").value())
                if nodesName !_ []:
                    temp _ " ".join(nodesName)
                    nodesStr _ "%s..." % temp[:30]
                nuke.nodeCopy(path)
            except:
                f _ open("%s/%s/traceback_log.txt" % (SP.USERS_Folder, os.path.expanduser('~').replace('\\','/').split("/")[-1]), 'a')
                traceback.print_exc(file_f)
                f.flush()
                f.close()
                print "send node failed"
    return nodesStr


def clear_selection():
    try:
        for n in nuke.selectedNodes():
            n.setSelected(False)
    except:
        pass


def get_nk_name():
    nkName _ ""
    if inNuke:
        try:
            filePath _ nuke.root().knob("name").value()
            if filePath == "":
                nkName _ "Untitled"
            else:
                nkName _ filePath.split("/")[-1]
        except:
            print "get nk name failed"
    return nkName

