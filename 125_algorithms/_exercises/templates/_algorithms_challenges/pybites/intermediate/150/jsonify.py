# _______ j__
# _______ __
#
# members """
# id,first_name,last_name,email
# 1,Junie,Kybert;jkybert0@army.mil
# 2,Sid,Churching|schurching1@tumblr.com
# 3,Cherry;Dudbridge,cdudbridge2@nifty.com
# 4,Merrilee,Kleiser;mkleiser3@reference.com
# 5,Umeko,Cray;ucray4@foxnews.com
# 6,Jenifer,Dale|jdale@hubpages.com
# 7,Deeanne;Gabbett,dgabbett6@ucoz.com
# 8,Hymie,Valentin;hvalentin7@blogs.com
# 9,Alphonso,Berwick|aberwick8@symantec.com
# 10,Wyn;Serginson,wserginson9@naver.com
# """
#
#
# ___ convert_to_json members_?
#     members_data    # list
#     ___ i row __ e.. ?.s.. "\n" .s.. "\n"
#         __ i __ 0
#             row ?.s.. ","
#             id_h, first_h, last_h, email_h ? 0 ? 1 ? 2 ? 3
#         ____
#             row_split __.s.. "[|,;]" ?
#             ?.a.. ?
#
#     members_stg    # list
#     ___ member __?
#         member_dict
#             ? ? 0
#             ? ? 1
#             ? ? 2
#             ? ? 3
#
#
#         ?.a.. ?
#
#     members_json j__.d..?
#     r.. ?