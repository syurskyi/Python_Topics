____ emoji _______ what_means_emoji, find_emoji


___ test_what_means_emoji_found
    what_means_emoji('🐶').l.. __ 'dog face'
    what_means_emoji('🏋').l.. __ 'weight lifter'
    what_means_emoji('🌇').l.. __ 'sunset over buildings'


___ test_what_means_emoji_not_found
    ... what_means_emoji('aaa').l.. __ 'not found'


___ test_find_matches(capfd):
    find_emoji('sun')
    output = ?.r .. 0].l..
    # some of the results you should get back
    ... 'sunrise' __ output
    ... '🌅' __ output
    ... 'sunset over buildings' __ output
    ... '🌇' __ output
    ... 'sun with face' __ output
    ... '🌻' __ output


___ test_find_no_match(capfd):
    find_emoji('awesome')
    output = ?.r .. 0].l..
    ... n.. output.s.. o. 'no matches' __ output.l..