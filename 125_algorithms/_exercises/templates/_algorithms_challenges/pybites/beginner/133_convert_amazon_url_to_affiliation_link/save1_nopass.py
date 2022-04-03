# ___ generate_affiliation_link url
#     sub_str1  "/dp"
#     sub_str2  ".com/"
#     start_occurrence  ?.f.. ?
#     mid_occurrence  ?.f.. ?
#     value  0
#     ___ i __ r.. 0, ?
#         start_chop  ?.f.. ? v.. + 4
#     ___ i __ r.. 0, m..
#         mid_chop  ?.f.. ? v..
#     end_chop  ?.r.. '/', 1 1
#     front_?  ? |s__.r.. "https:", "http:"
#     mid_url  ? m..| .r.. e.. ""
#     tag  "?tag=pyb0f-20"
#     r.. _ _ _ .f.. ? ? ?