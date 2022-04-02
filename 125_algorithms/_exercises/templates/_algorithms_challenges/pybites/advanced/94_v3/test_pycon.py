____ copy _______ d..

_______ p__

____ pycon _______ (load_pycon_data,
                   get_most_popular_talks_by_views,
                   get_most_popular_talks_by_like_ratio,
                   get_talks_gt_one_hour,
                   get_talks_lt_twentyfour_min)


?p__.f..(scope='module')
___ videos
    r.. load_pycon_data()


___ test_load_pycon_data(videos
    ... l..(videos) __ 147
    ... isi..(videos[0], t..)


___ test_get_most_popular_talks_by_views(videos
    # as sort might be used in place, or any other list manipulation
    # let's make sure we work with a copy of the module fixture
    videos_copy = d..(videos)
    expected =  'T-TwcmT6Rcw', 'GBQAKldqgZs', 'ms29ZPUKxbU',
                'zJ9z6Ge-vXs', 'WiQqqB9MlkA'
    vids = l..(get_most_popular_talks_by_views(videos_copy))
    actual = [vid.id ___ vid __ vids[:5]]
    ... expected __ actual


___ test_get_most_popular_talks_by_like_ratio(videos
    # same here: let's use a local copy of videos
    videos_copy = d..(videos)
    vids = l..(get_most_popular_talks_by_like_ratio(videos_copy))
    expected =  '8OoR-P6wE0M', 'h-38HZqanJs', 'C7ZhMnfUKIA',
                'GmbaKdd6o6A', '3EXvR1shVFQ'
    actual = [vid.id ___ vid __ vids[:5]]
    ... expected __ actual


___ test_get_talks_gt_one_hour(videos
    vids = get_talks_gt_one_hour(videos)
    ... vids[0].id __ '0hsKLYfyQZc'
    ... vids[-1].id __ 'ZwvjtCjimiw'
    ... l..(vids) __ 35


___ test_get_talks_lt_twentyfour_min(videos
    vids = get_talks_lt_twentyfour_min(videos)
    ... vids[0].id __ 'zQeYx87mfyw'
    ... vids[-1].id __ 'TcHkkzWBMKY'
    ... l..(vids) __ 12