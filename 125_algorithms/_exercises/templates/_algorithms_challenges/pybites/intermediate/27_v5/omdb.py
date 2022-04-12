# _______ glob
# _______ j__
# _______ __
# _______ __
# ____ u__.r.. _______ u..
#
# BASE_URL 'http://projects.bobbelderbos.com/pcc/omdb/'
# MOVIES ('bladerunner2049 fightclub glengary '
#           'horrible-bosses terminator').s..
# TMP '/tmp'
#
# # little bit of prework (yes working on pip installables ...)
# ___ movie __ ?
#     fname _* ?.json
#     remote __.p...j.. B.. ?
#     local __.p...j.. T.. ?
#     u.. ? ?
#
# files glob.g.. __.p...j.. T.. '*json'
#
#
# ___ get_movie_data files=files
#     result    # list
#     ___ file __ ?
#         w__ o.. ? __ f
#             ?.a.. j__.l.. f
#     r.. ?
#
#
# ___ get_single_comedy movies
#     r.. m 'Title'  ___ ? __ ? __ 'Comedy' __ ? 'Genre' .s.. ', ' 0
#
#
# ___ get_movie_most_nominations movies
#     r __.c.. _ (\d+) nomin'
#     r.. s.. m 'Title'  ? 'Awards'  ___ ? __ ? k.._l.... x i.. r.f.. ? 1 0 -1 0
#
#
# ___ get_movie_longest_runtime movies
#     r __.c.. _ (\d+) min
#     r.. s.. m 'Title'  i.. ?.f.. ? 'Runtime' 0 ___ ? __ ? k.._l.... x| -? 1 0 0
