# ____ a___.a.. ______ A..
# ____ a___.d... ______ D..
# ____ a___.s... ______ S..
#
# ____ a_c.. ______ AOC.. AfC..
# ____ d_c.. ______ DLC.. DUC..
# ____ s_c.. ______ SAC.. SDC..
# ____ m_a.. ______ MA..
#
# # instantiate new objects
# menu_action _ M..
# frontdoor _ D.. 'Front Door
# frontdoor_lock _ DLC.. ?
# frontdoor_unlock _ DUC.. ?
#
# # Set up the commands
# m_a__.set_command(f_d.. f_l.. f_u..
#
# # Try the commands with undo
# m_a__.a.. f_d..
# m_a__.d.. f_d..
# m_a__.d.. f_d..
# m_a__.u..
# m_a__.u..
# m_a__.u..
#
# # Extra undo to test empty queue
# m_a__.u..
#
