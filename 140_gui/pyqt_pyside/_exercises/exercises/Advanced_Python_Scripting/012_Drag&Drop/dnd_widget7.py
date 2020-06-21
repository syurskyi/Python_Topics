# _____ ___
# _____ __
# ____ ?.?C.. _____ _
# ____ ?.?G.. _____ _
#
# icon _ __.pa__.j.. __.pa__.d_n.. -d 'drag.png'
#
# c_ listWidgetClass ?LW..
#     ___  -
#         s__ ? . -
#         sWF.. __.WSOTH..
#         sDDM.. ?AIV...DD..
#         sSM.. ?AIV...ES..  # vjlychaet vozmoznost' vudeljat' neskol'ko fajlov
#         files _ # list
#
#     ___ dropEvent  event
#         # print 'DROP', type(event)
#         mimedata _ ?.mD..
#         __ ?.hU..
#             ___ f __ ?.u..
#                 aF.. ?.tLF..
#
#     ___ dragEnterEvent  event
#         __ ?.source __ ____
#             ?.i..
#         ____
#             ? _ ?.mD..
#             __ ?.hU..
#                 ?.a..
#             ____
#                 ?.i..
#
#     ___ dragMoveEvent  event
#         __ ?.source __ ____
#             ?.i..
#         ____
#             ? _ ?.mD..
#             __ ?.hU..
#                 ?.a..
#             ____
#                 ?.i..
#
#     ___ startDrag  dropAction     # pereopredeljaem method kotoruj otvechaet za to shto proishodit kogda mu nachinaem shto to peretaskivat'
#                                          # dropAction odin iz rezimov peretaskivanija
#         drag _ ?D..               # nyzno sozdat' klass kotoruj otvechaet za peretaskivanie dannuh i eto ne mimedata a klass QDrag. QDrag dolzen znat' komy on prenadlezit
#         mimedata _ ?MD..           # i sootvestvenno mimedata kotorue bydyt tam lezat'
#         url _ # list                        # potom nado sobrat' danue kotorue mu hotim pomestit' v ety mimedata a eto y nas pyti k fajlam iz vudelenuh fajlov
#         ___ i __ sI..(  # dlja vudelenuh elementov mu zabiraem pyt' i kladjom v url
#             u__.ap.. ?.d.. __.UR..
#         print u..
#         ?.sU.. ?U_.fLF..(x) ___ ? __ u..  # kogda mu polychili pyti nam nado ih polozit' v mimedata. preobrazovuvaem strochky v klass QUrls
#                                                                 # kazduj pyt' kotoruj est' v spiske preobrazovuvaetsja v QUrl. Generator vernjot nam spisok etih klassov
#         drag.sMD.. m..                              # polychennue dannue mu lozim v objekt draga, toest' v etot kontejner dlja peretaskivanija
#         pix _ ?P.. i..
#         d__.sP.. ?
#         r _ d__.e..                                        # exec_ kak iv dialogah vozvrachaet kakoj to rezyl'tat
#         print ?
#         __ r __ __.DA...MA..                       # esli y nas yspesho proizvedeno peretaskivanie to mu ydaljaem nashi vudelenue items
#             dS..                              # metod deleteSelected
#
#     ___ aF..  path
#         __ no. ? __ files
#             item _ ?LWI..
#             ?.sT.. __.pa__.b.. ?
#             ?.sD.. __.UR.. ?
#             f__.ap.. ?
#
#     ___ deleteSelected
#         ___ s __ sI..                       # perebiraem vse vudelenue elementu
#             f__.r.. ?.d.. 32                     # zabirajy pyt' kotoruj lezit v data i ydaljay iz svoego byfera
#             tI.. iFI.. ? .r..        # posle chego ydaljay sam item
#
# __ _____ __ ______
#     app _ ?A..
#     w _ ?
#     ?.s..
#     ?.e..