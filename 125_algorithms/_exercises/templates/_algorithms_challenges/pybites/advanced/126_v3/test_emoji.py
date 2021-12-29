____ emoji _______ what_means_emoji, find_emoji


___ test_what_means_emoji_found():
    what_means_emoji('🐶').lower() __ 'dog face'
    what_means_emoji('🏋').lower() __ 'weight lifter'
    what_means_emoji('🌇').lower() __ 'sunset over buildings'


___ test_what_means_emoji_not_found():
    ... what_means_emoji('aaa').lower() __ 'not found'


___ test_find_matches(capfd):
    find_emoji('sun')
    output = capfd.readouterr()[0].lower()
    # some of the results you should get back
    ... 'sunrise' __ output
    ... '🌅' __ output
    ... 'sunset over buildings' __ output
    ... '🌇' __ output
    ... 'sun with face' __ output
    ... '🌻' __ output


___ test_find_no_match(capfd):
    find_emoji('awesome')
    output = capfd.readouterr()[0].lower()
    ... n.. output.s.. o. 'no matches' __ output.lower()