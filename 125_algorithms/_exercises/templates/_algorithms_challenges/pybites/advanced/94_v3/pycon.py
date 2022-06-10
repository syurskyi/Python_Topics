# _______ __
# _______ p..
# _______ __
# _______ u__.r..
# ____ c.. _______ n..
# ____ d__ _______ t..
#
# # prework
# # download pickle file and store it in a tmp file
# pkl_file 'pycon_videos.pkl'
# data 'http://projects.bobbelderbos.com/pcc/{}'.f.. ?
# pycon_videos __.p...j.. '/tmp', ?
# u__.r...u.. ? ?
#
# # the pkl contains a list of Video namedtuples
# Video n..('Video', 'id title duration metrics')
#
#
# ___ load_pycon_data pycon_videos_?
#     """Load the pickle file (pycon_videos) and return the data structure
#        it holds"""
#     w__ o.. ? __ __ pkl
#         r.. p...l.. ?
#
#
# ___ get_most_popular_talks_by_views videos
#     """Return the pycon video list sorted by viewCount"""
#     r.. s.. ? k.._l.... vid -i.. ?.m.. 'viewCount'
#
#
# ___ _like_ratio vid
#     metrics ?.m..
#     r.. - f__ ? 'likeCount' ) - f__(? 'dislikeCount'  / f__ ? 'viewCount'
#
#
# ___ get_most_popular_talks_by_like_ratio videos
#     """Return the pycon video list sorted by most likes relative to
#        number of views, so 10 likes on 175 views ranks higher than
#        12 likes on 300 views. Discount the dislikeCount from the likeCount.
#        Return the filtered list"""
#     r.. s.. ? key=_l..
#
#
# duration_regex __.c.. _ PT(?:(?P<hrs>\d+)H)?(?:(?P<mins>\d+)M)?(?:(?P<secs>\d+)S)?
#
#
# ___ _vid_time vid
#     time_parts d__.m.. ?.d.. .g.. d.._0
#     r.. t.. h.._i.. ? hrs m.._i.. ? mins s.._i.. ? secs
#
#
# ___ get_talks_gt_one_hour videos
#     """Filter the videos list down to videos of > 1 hour"""
#     r.. vid ___ ? __ ? __ _v.. ? > t.. h.._1
#
#
# ___ get_talks_lt_twentyfour_min videos
#     """Filter videos list down to videos that have a duration of less than
#        24 minutes"""
#     r.. vid ___ ? __ ? __ _? ? < t.. m.._24
