_______ __
_______ p..
_______ __
_______ u__.r..
____ c.. _______ n..
____ d__ _______ t..

# prework
# download pickle file and store it in a tmp file
pkl_file 'pycon_videos.pkl'
data 'http://projects.bobbelderbos.com/pcc/{}'.f..(pkl_file)
pycon_videos __.p...j..('/tmp', pkl_file)
u__.r...u.. ? pycon_videos)

# the pkl contains a list of Video namedtuples
Video n..('Video', 'id title duration metrics')


___ load_pycon_data(pycon_videos=pycon_videos
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    w__ o.. pycon_videos, 'rb') __ pkl:
        r.. p...l.. pkl)


___ get_most_popular_talks_by_views(videos
    """Return the pycon video list sorted by viewCount"""
    r.. s..(videos, k.._l.... vid: -i..(vid.metrics 'viewCount'


___ _like_ratio(vid
    metrics vid.metrics
    r.. -(f__(metrics 'likeCount' ) - f__(metrics 'dislikeCount'  / f__(metrics 'viewCount' )


___ get_most_popular_talks_by_like_ratio(videos
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    r.. s..(videos, key=_like_ratio)


duration_regex __.c.. _ PT(?:(?P<hrs>\d+)H)?(?:(?P<mins>\d+)M)?(?:(?P<secs>\d+)S)?')


___ _vid_time(vid
    time_parts duration_regex.m..(vid.duration).groupdict(default=0)
    r.. t..(h.._i..(time_parts 'hrs' ), m.._i..(time_parts 'mins' ), s.._i..(time_parts 'secs'


___ get_talks_gt_one_hour(videos
    """Filter the videos list down to videos of > 1 hour"""
    r.. [vid ___ vid __ videos __ _vid_time(vid) > t..(h.._1)]


___ get_talks_lt_twentyfour_min(videos
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    r.. [vid ___ vid __ videos __ _vid_time(vid) < t..(m.._24)]
