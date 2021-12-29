_______ os
_______ pickle
_______ re
_______ urllib.request
____ collections _______ namedtuple
____ datetime _______ timedelta

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = 'http://projects.bobbelderbos.com/pcc/{}'.format(pkl_file)
pycon_videos = os.path.join('/tmp', pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


___ load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, 'rb') as pkl:
        r.. pickle.load(pkl)


___ get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    r.. s..(videos, key=l.... vid: -int(vid.metrics['viewCount']))


___ _like_ratio(vid):
    metrics = vid.metrics
    r.. -(float(metrics['likeCount']) - float(metrics['dislikeCount'])) / float(metrics['viewCount'])


___ get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    r.. s..(videos, key=_like_ratio)


duration_regex = re.compile(r'PT(?:(?P<hrs>\d+)H)?(?:(?P<mins>\d+)M)?(?:(?P<secs>\d+)S)?')


___ _vid_time(vid):
    time_parts = duration_regex.match(vid.duration).groupdict(default=0)
    r.. timedelta(hours=int(time_parts['hrs']), minutes=int(time_parts['mins']), seconds=int(time_parts['secs']))


___ get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    r.. [vid ___ vid __ videos __ _vid_time(vid) > timedelta(hours=1)]


___ get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    r.. [vid ___ vid __ videos __ _vid_time(vid) < timedelta(minutes=24)]
