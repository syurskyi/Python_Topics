# ____ ______._G.. _____ _
# ____ ______._C.. _____ _
# ____ ______._W.. _____ _
# _____ __
# _____ j..
#
# HOME_FOLDER _ __.pa__.j.. __.pa__.d..  -f 'icons'
#
#
# c_ Panel _W..
#     ___  -
#         s__ P..  . -
#         r.. 400 400
#         mouse_position _ _C.. .p..
#         m.. ? - _P.. 200 200
#         sMT.. T..
#         sWF.. __.FWH.. / __.P..
#         sA.. __.WA_QOC..
#
#         selected_item _ N..
#
#         mouse_destination _ _P.. w.. /2 h.. /2
#
#         layout _ _GL..
#         ?.aW.. ActionLabel 1), 0, 0)
#         ?.aW.. ActionLabel 2), 0, 1)
#         ?.aW.. ActionLabel 3), 0, 2)
#         ?.aW.. ActionLabel 4), 1, 0)
#         ?.aW.. ActionLabel 5), 1, 2)
#         ?.aW.. ActionLabel 6), 2, 0)
#         ?.aW.. ActionLabel 7), 2, 1)
#         ?.aW.. ActionLabel 8), 2, 2)
#
#         sL.. ?
#
#         action_path _ __.pa__.j.. H.. "actions"
#         __ no. __.pa__.e.. ?
#             __.m_d_ ?
#
#     ___ keyReleaseEvent  event
#         __ ?.iAR..
#             r_
#         __ ?.t.. __ "n"
#             __ selected_item __ N..
#                 c..
#                 r_
#             ex__ ?.co..
#             c..
#
#     ___ paintEvent _PE..
#         s__ P.. .pE.. _PE..
#         painter _ _P..
#
#         draw_line ?
#         s_l_c..
#
#         nuke_image _ _P.. "@/nuke.png" @ H..
#         p__.dP.. _P.. w.. /2-24 h.. /2-24) ?
#
#     ___ set_label_color
#         widgets _ l__.iA. i .w.. ___ ? __ ra.. l__.c..
#         selected_item _ N..
#         ___ w __ widgets
#             __ l__.in.. ?.g..
#                 ?.s_s.. T..
#                 s__ _ w
#             ____
#                 w.set_selected F..
#
#     ___ draw_line painter
#         pen _ _P.. _C.. 0,0,0
#         ?.sW.. 2
#         p__.sP.. ?
#         center _ _P.. w../2 h../2
#         destination _ m..
#         line _ _P.. c.. c..+_P.. 1 0 d.. d..+_P.. -1 0
#         p__.dP.. ?
#
#     ___ mouseMoveEvent event
#         mouse_destination _ ?.p..
#         u..
#
#     ___ keyPressEvent event
#         __ ?.iAR..
#             r_
#
#
# c_ Dialog _D..
#     ___  -  id
#         s__ D..  . -
#
#         ? _ ?
#         action_path _ __.pa__.j.. H.. "actions" "@.txt"  ?
#         name_label _ _L.. "Name:"
#         name_line_edit _ _LE..
#         code_plain_text _ _PTE..
#
#         name_layout _ _HBL..
#         ?.aW.. n_l..
#         ?.aW.. n_l_e..
#
#         master_layout _ _VBL..
#         ?.addLayout n..
#         ?.aW.. c_p_t..
#
#         buttons _ _DBB_ _DBB_.Ok / _DBB_.C.. __.H..
#         m__.aW.. ?
#
#         ?.a__.c.. a..
#         ?.r__.c.. r..
#
#         sL.. m..
#         l_a..
#
#     ___ load_action
#         __ __.pa__.e.. a..
#             doc _ j...l.. o.. a..
#             name _ ? 'name'
#             code _ ? 'code'
#             n_l_e_.sT.. n..
#             c_p_t_.sPT.. c..
#
#     ___ save_action
#         doc _ di__
#         ? 'name' _ n_l_e_.t..
#         ? 'code' _ c_p_t_.tPT..
#         pa__ _ o.. a_p.. _
#         j...d.. ? pa__
#
#
# c_ ActionLabel _L..
#     ___  -  id
#         s__ ? . -
#
#         id _ id
#         sA.. __.AC..
#         sMT.. T..
#         sFW.. 100
#         sFH.. 25
#         sSS.. """background:red;
#                             color:black"""
#         ?
#
#     ___ set_action
#
#         pa__ _ __.pa__.j.. H.. "actions", "@.txt" % ?
#         __ __.pa__.e.. pa__
#             doc _ j...l.. o.. pa__
#             name _ d.. 'name'
#             code _ d.. 'code'
#         ____
#             name _ "Action @ "  ?
#             code _ ""
#
#         sT.. n..
#         c.. _ c..
#
#     ___ mousePressEvent event
#         __ ?.b.. __ __.RB..
#             dialog _ D.. i.
#             __ ?.ex_
#                 ?.s_a..
#             p__ .cl..
#
#     ___ set_selected is_selected
#
#         __ ?
#                 sSS..("""background:green;
#                             color:black""")
#         ____
#             sSS..("""background:red;
#                             color:black""")
# ___ start
#     ?.p.. _ P..
#     ?.p__.s..