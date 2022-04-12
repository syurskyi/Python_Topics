# _______ j__
#
#
# ___ get_movie_data files l.. __ l..
#     """Parse movie json files into a list of dicts"""
#     movie_files    # list
#     ___ file __ ?
#         w__ o.. ? __ mf
#             data j__.l.. ?
#             ?.a.. ?
#     r.. ?
#
#
# ___ get_single_comedy movies l.. __ s..
#     """return the movie with Comedy in Genres"""
#     ___ movie __ ?
#         __ "Comedy" __ ? "Genre"
#             r.. ? "Title"
#
#
# ___ get_movie_most_nominations movies l.. __ s..
#     """Return the movie that had the most nominations"""
#     nominations_dict    # dict
#     ___ movie __ ?
#         nominations_index ? "Awards" .r.. "nominations"
#         nominations_count ? "Awards" ? -3| ?
#
#         __ ? "Title" n.. __ ?
#             ? ? "Title" i.. ?
#
#     r.. m.. n.. k.._n__.g..
#
#
# ___ get_movie_longest_runtime movies l.. __ s..
#     """Return the movie that has the longest runtime"""
#     runtime_dict    # dict
#     ___ movie __ ?
#         runtime_index ? "Runtime" .r.. " min"
#         movie_runtime ? "Runtime" |?
#
#         __ ? "Title" n.. __ r..
#             ? ? "Title" i.. m..
#
#     r.. m.. ? k.._r__.g..
#
# #if __name__ == "__main__":
#     #print(get_movie_most_nominations(get_movie_data(data)))
#     #print(get_movie_longest_runtime(get_movie_data(data)))