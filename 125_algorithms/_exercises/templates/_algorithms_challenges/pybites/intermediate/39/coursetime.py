# ____ d__ _______ d__, t..
# _______ __
# _______ __
# _______ u__.r..
#
# # getting the data
# COURSE_TIMES __.p...j..
#     __.g.. TMP  /tmp,
#     'course_timings'
#
# u__.r...u..
#     'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
#     C..
#
#
#
# ___ get_all_timestamps
#     """Read in the COURSE_TIMES and extract all MM:SS timestamps.
#        Here is a snippet of the input file:
#
#        Start  What is Practical JavaScript? (3:47)
#        Start  The voice in your ear (4:41)
#        Start  Is this course right for you? (1:21)
#        ...
#
#         Return a list of MM:SS timestamps
#     """
#     w__ o.. C.. __ file
#         course_timestamps    # list
#         file_lines ?.r..
#         ___ line __ ?
#             ts __.f.. _ (\d{1,2}?:\d{1,2}) ?
#             __ ?
#                 ?.a.. ? 0
#
#         r.. ?
#
#
# ___ calc_total_course_duration timestamps
#     """Takes timestamps list as returned by get_all_timestamps
#        and calculates the total duration as HH:MM:SS"""
#     dt_conversion  d__.s.. ? '_M:_S' ___ ? __ ?
#     baseline d__ 1900, 1, 1, 0, 0, 0
#     ___ course_dt __ d..
#         baseline ? + t.. minutes_?.m.. s.._c...s..
#
#     r.. ?.s.. '_-H:_M:_S
#
#
# #if __name__ == "__main__":
#     #print(get_all_timestamps())
#     #print(calc_total_course_duration(get_all_timestamps()))