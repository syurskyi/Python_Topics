# ____ d__ _______ t..
# ____ t___ _______ L..
#
#
# ___ get_srt_section_ids text s.. __ L.. i..
#     """Parse a caption (srt) text passed in and return a
#        list of section numbers ordered descending by
#        highest speech speed
#        (= ratio of "time past:characters spoken")
#
#        e.g. this section:
#
#        1
#        00:00:00,000 --> 00:00:01,000
#        let's code
#
#        (10 chars in 1 second)
#
#        has a higher ratio then:
#
#        2
#        00:00:00,000 --> 00:00:03,000
#        code
#
#        (4 chars in 3 seconds)
#
#        You can ignore milliseconds for this exercise.
#     """
#
#     text ?.s..
#
#     sections ?.s.. '\n\n'
#
#
#     id_to_speed    # dict
#     ___ section __ ?
#         parts ?.s.. '\n'
#
#         id_,times,text parts
#
#         start_time,end_time t__.s.. '-->'
#
#         tds    # list
#         ___ t__ __ ? ?
#             hours,minutes,seconds t__.s.. ':'
#             hours i.. ?
#             minutes i.. h..
#             seconds f__ '.'.j.. ?.s.. ','
#             td t.. h.._? m.._?s.._?
#             tds.a.. ?
#
#
#         time_elapsed ? 1 - ? 0.t..
#         characters l.. t..
#
#         characters_per_second ?/t..
#
#
#         i.. i.. id_   ?
#
#
#
#
#     r.. s.. l.. i__.k.. k.._l.... x i.. ? r.._T..
#
#
#
#
#
#
#
#
#
#
#
#
