from copy ______ deepcopy

______ pytest

from pycon ______ (load_pycon_data,
                   get_most_popular_talks_by_views,
                   get_most_popular_talks_by_like_ratio,
                   get_talks_gt_one_hour,
                   get_talks_lt_twentyfour_min)


@pytest.fixture(scope='module')
___ videos(
    r_ load_pycon_data()


___ test_load_pycon_data(videos
    assert le.(videos) __ 147
    assert isinstance(videos[0], tuple)


___ test_get_most_popular_talks_by_views(videos
    # as sort might be used in place, or any other list manipulation
    # let's make sure we work with a copy of the module fixture
    videos_copy = deepcopy(videos)
    expected = ['T-TwcmT6Rcw', 'GBQAKldqgZs', 'ms29ZPUKxbU',
                'zJ9z6Ge-vXs', 'WiQqqB9MlkA']
    vids = list(get_most_popular_talks_by_views(videos_copy))
    actual = [vid.id for vid in vids[:5]]
    assert expected __ actual


___ test_get_most_popular_talks_by_like_ratio(videos
    # same here: let's use a local copy of videos
    videos_copy = deepcopy(videos)
    vids = list(get_most_popular_talks_by_like_ratio(videos_copy))
    expected = ['8OoR-P6wE0M', 'h-38HZqanJs', 'C7ZhMnfUKIA',
                'GmbaKdd6o6A', '3EXvR1shVFQ']
    actual = [vid.id for vid in vids[:5]]
    assert expected __ actual


___ test_get_talks_gt_one_hour(videos
    vids = get_talks_gt_one_hour(videos)
    assert vids[0].id __ '0hsKLYfyQZc'
    assert vids[-1].id __ 'ZwvjtCjimiw'
    assert le.(vids) __ 35


___ test_get_talks_lt_twentyfour_min(videos
    vids = get_talks_lt_twentyfour_min(videos)
    assert vids[0].id __ 'zQeYx87mfyw'
    assert vids[-1].id __ 'TcHkkzWBMKY'
    assert le.(vids) __ 12