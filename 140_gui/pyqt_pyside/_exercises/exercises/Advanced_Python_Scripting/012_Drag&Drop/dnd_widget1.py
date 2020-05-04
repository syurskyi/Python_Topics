# _____ ___
# _____ __
# ____ ?.?C.. _____ _
# ____ ?.?G.. _____ _
#
# c_ listWidgetClass ?LW..
#     ___  -
#         s__ ? . -
#         sWF.. __.WSOTH..)         # #okno bydet vsegda poverh drygih okon
#         sDDM.. ?AIV...DO..      # shto bu dropEvent zarabotal nado vklychit dlja etogo vidgeta setDragDropMode
#
#     ___ dropEvent event                # to shto proishodit kogda mu sbrasuvaem dannue na vidget
#         print 'DROP', ty.. ?
#         mimedata _ ?.mD..            # kogda mu peretaskivaem element, to pomimo togo shto srabatuvaet DropEvent,
#                                                # srabatuvaet echjo 2 eventa, dragEnterEvent and dragMoveEvent
#                                                # obuchno oni odinakovue i govorjat mozet li nash vidget prinjat' eti dannue kotorue mu peretaskivaem
#                                                # i vnytri etogo eventa kak raz proverjaetsja kakogo tipa dannue k nam prishli
#                                                # i etot event dolzen skazat' mozet li nash event eti dannue prinjat'
#         __ ?.hT..
#             print 'text'
#         ____ ?.hU..
#             print 'urls'
#
#     ___ dragEnterEvent event
#         ?.a..
#         print 'ENTER', ty.. ?
#
#     ___ dragMoveEvent  event
#         ?.a..
#         print 'MOVE'
#
# __ _____ __ ______
#     app _ ?A..
#     w _ ?
#     w.s..
#     ?.e..