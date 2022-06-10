# ____ c.. _______ n..
# _______ __
# _______ p..
# _______ u__.r..
# _______ __
#
# # prework
# # download pickle file and store it in a tmp file
# pkl_file 'pycon_videos.pkl'
# data _*https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
# tmp  __.g.. TMP  /tmp
# pycon_videos __.p...j.. ? p..
# u__.r...u.. ? ?
#
# # the pkl contains a list of Video namedtuples
# Video n..('Video', 'id title duration metrics')
#
#
# ___ load_pycon_data pycon_videos_?
#     """Load the pickle file (pycon_videos) and return the data structure
#        it holds"""
#
#     r.. p...l.. o.. ? __
#
#
# ___ get_most_popular_talks_by_views videos
#     """Return the pycon video list sorted by viewCount"""
#
#
#
#     r.. s.. ? r.._T..k.._l.... x i.. ?.m.. 'viewCount'
#
#
# ___ get_most_popular_talks_by_like_ratio videos
#     """Return the pycon video list sorted by most likes relative to
#        number of views, so 10 likes on 175 views ranks higher than
#        12 likes on 300 views. Discount the dislikeCount from the likeCount.
#        Return the filtered list"""
#
#
#     r.. s.. ? r.._T..k.._l.... x i.. ?.m.. 'likeCount' ) - i.. ?.m.. 'dislikeCount' /i.. ?.m.. 'viewCount'
#
#
# ___ get_talks_gt_one_hour videos
#     """Filter the videos list down to videos of > 1 hour"""
#
#
#     r.. video ___ ? __ ? __ 'H' __ ?.d..
#
#
# ___ get_talks_lt_twentyfour_min videos
#     """Filter videos list down to videos that have a duration of less than
#        24 minutes"""
#
#     r.. video ___ ? __ ? __ ('H' n.. __ ?.d.. a.. i.. __.s.. _ (\d+)M ?.d.. .g.. 1 < 24
#
#
# __ _______ __ _______
#
#     print ? 0.d..
