# ______ ___
# ______ l__
# ____ ?.__ ______ ?SI.. ?TWI.. ?M.. ?A.. __ \
#     ?MB..
# ______ ?
# ____ utils.MongoUtils ______ MongoUtils
# ______ ____
# ______ t__
# ____ ? ______ ?G..
# ______ m__
# ______ t__
# ______ __
# __ ___.version>'3':
#     ______ _t.. __ t..
# ____
#     ______ t..
# '''
# @property  mainWindow:QMainWindow
# @property  ui:MainWindow
# '''
# c_ AppController o..
#     '''
#     classdocs
#     '''
#
#
#     ___ oCM..
#         l__.i.. cD.+"."+cC..
#         page _ 1
#         queryjson _    # dict
#
#         ?.s_n_t.. fR.., |cD. cC.. q_j.. p.. l..
# #         self.findRecord(self.curDb,self.curCol,self.queryjson,self.page,self.limit)
#
#
#     ___  -   app
#         '''
#         Constructor
#         '''
#         ? ?
#         sM.. ?.mRM..
#         setView ?.uMW..
#         mainWindow _ ?.mW..
#         mgutils _ MU..
#         sortCondition _ N..
#         log _ l__.gL.. "AppController
#
#         limit _ 20
#
#         ctxAction _ ?A.. "Find",ui.tW__
#         ?.t___.c__ oCM..
#
#     ___ connectServer
#         t__.s_n_t.. _cS..
#
#     ___ _connectServer
#         ui.cB__.sE.. F..
#         host _ ui.mH__.t..
#
#         __ host __ ""
#             host _ "localhost"
#
#         ___
#             indexOfSep _ h__.i.. ":"
#             hostName, portStr _ host.s.. ":"
#             port _ in. pS..
#         ______ V.. __ e
#             hostName _ h..
#             port _ 27017
#
#         ___
#             conn _ ?.C.. hN... p..
#             sM.. "connect " + h.. + " success!"
#             databases _ c__.d_n..
#
#
#
#             colsMap _    # dict
#             ___ db __ d..
#                 cM..|? _ c..|?.c_n..
#
#             ui.tW__.c..
#             treeItems _   # list
#             ___ db __ d..
#                 dbItem _ ?TWI.. ui.tW__ |?
#                 tI__.ap.. ?
#                 cols _ cM..|?
#                 ___ col __ ?
#                     colItem _ ?TWI.. dI.. |?
#
#
#             ui.tW__.iTLI.. 0 tI..
#             l__.i.. d..
#
#         ______ E.. __ e
#             l__.e.. ?
#             errorMsg _ h.. +" connect failed:" + ?.m..
#             sM.. ?
#             t__.print_exc file____.s_o..
#
#         ui.cB__.sE.. T..
#
#
#     ___ query
#         mRM...c..
#         query _ ui.q__.t..
#         query _ __.sub _*(,?)(\w+?)\s*?:", r"\1'\2':", q.. .r.. "'", "\""
#
#
#         tI.. _ ui.tW__.cI..
#         dbTreeItem _ ?.p..
#
#         page _ 1
#
#         __ dbTreeItem __ N..
#             sM.. "please select a collection"
#             r_
#
#         collName _ tI...t.. 0
#         dbName _ dTI__.t.. 0
#
#         curCol _ cN..
#         curDb _ dN..
#
#
#         limit _ limit
#
#
#         ___
#             __ query __ ""
#                 q_j.. _    # dict
#             ____
#                 q_j.. _ ____.lo.. ?
#
#
#             q_j.. _ q_j..
# #             self.findRecord(dbName,collName,queryjson,self.page,limit)
#             t__.s_n_t.. fR.. |cD. cC.. qj.. p.. l..
#
#         ______ E.. __ e
#             l__.e.. ?
#             sM.. ?.m..
#             t__.print_exc file____.s_o..
#         #db = self.conn[selectDb]
#
#
#     ___ findRecord  dbName collName queryjson page limit
#         ui.q_b_.sE.. F..
#         preview _ mgu__.p.. cN.. qj.. p.. l.. sC..
#         ui.p__.sT.. ?
#
#         ui.pB...sE.. p.. > 1
#
#
#
#         db _ c..|dN..
#         coll _ ?|cN..
#
#
#
#
#         skipnum _ p.. - 1) * l..
#
#         start _ t__.t__
#         __ sortCondition __ N..
#             cursor _ c__.f.. qj.. .l.. l.. .s.. s..
#         ____
#             mgSort _   # list
#             ___ k,v __ sC__.i..
#                 mS__.ap.. ? ?
#
#             cursor _ c__.f.. qj.. .s.. mS.. .l.. l.. .s.. s..
#
#         totalCounts _ c__.c..
#         pages _ in. m__.cei. tC../fl.. l..
#         ui.nB__.sE.. p.. < ?
#
#         ui.p__.sT.. st. p.. +"/"+st. p.. + " total:"+st. tC..
#
#         fillTable cu..
#         ui.q_b_.sE.. T..
#
#
#     ___ fillTable cursor
#         mRM...fMBC.. ?
#         end _ t__.t__
#         ui.q__.sT.. "query use:"+st.|'%.4f'  |e.. - s..||+" s"
#
#     ___ setView ui_mainWindow
#         ui _ u_mW..
#
#
#
#     ___ sM.. model
#         mongoResultModel _ ?
#
#     ___ clickTable
#         index _ ui.t_v_.cI..
# #         self.log.debug(str(index.row())+","+str(index.column())+" clicked")
#         selectClickValue _ mRM...d.. ?
#
#
#
#
#         ui.vDL__.sT.. sCV..
#
#
#
#     ___ aTQ..
#         index _ ui.t_v_.cI..
#         labels _ mRM...gL..
#         columnName _ l..|i__.c..
#
#
#         l__.d.. mRM...gMD.. i__.r.. cN..
#         qj..|cN.. _ mRM...gMD.. i__.r.. cN..
#         l__.d.. qj..
#         ui.q__.sT.. ____.d.. qj..
#
#     ___ cS.. index order
#         labels _ mRM...gL..
#         columnName _ ?|i..
#         __ order __ __.AO..
#             mongoSort _ 1
#         ____
#             mongoSort _ -1
#
#
#         sortCondition _ |cN.. : mS..
#         ui.s__.sT.. ____.d.. ?
#
#
#     ___ showTreeMenu point
#         item _ ui.tW__.iA. ?
#         __ ? !_ N.. an. i__.p.. !_ N..
#             curDb _ i__.p.. .t.. 0
#             curCol _ i__.t.. 0
#             ctxMenu _ ?M..
#             ?.aA.. cA..
#             ?.exec_ ?G...?C...po.
#
#
#
#     ___ showMsg msg
#         mW__.sB.. .sM.. ?
#
#
#     ___ prevPagination
#         pa.. -_ 1
#         p..
#
#     ___ nextPagination
#         pa.. +_ 1
#         p..
#
#     ___ pagination
# #         self.findRecord(self.curDb, self.curCol, self.queryjson, self.page, self.limit)
#         t_.s_n_t.. fR.. |cD. cC.. qj.. p.. l..
#
#     ___ queryChange text
#         __ ? __ ""
#             qj.. _   # dict
#
