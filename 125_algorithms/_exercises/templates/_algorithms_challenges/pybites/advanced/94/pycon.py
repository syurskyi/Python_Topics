____ collections _______ n..
_______ os
_______ pickle
_______ urllib.request
_______ __

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = f'https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.j..(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = n..('Video', 'id title duration metrics')


___ load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""

    r.. pickle.load(open(pycon_videos,'rb'))


___ get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    


    r.. s..(videos,r.._T..key=l.... x: i..(x.metrics['viewCount']))


___ get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""


    r.. s..(videos,r.._T..key=l.... x: (i..(x.metrics['likeCount']) - i..(x.metrics['dislikeCount']))/i..(x.metrics['viewCount']))


___ get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""


    r.. [video ___ video __ videos __ 'H' __ video.duration]


___ get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""

    r.. [video ___ video __ videos __ ('H' n.. __ video.duration a.. i..(__.s..(r"(\d+)M",video.duration).group(1)) < 24)]


__ __name__ __ "__main__":

    print(load_pycon_data()[0].duration)
