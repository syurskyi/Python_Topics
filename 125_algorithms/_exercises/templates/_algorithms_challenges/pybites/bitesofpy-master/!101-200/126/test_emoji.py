from emoji ______ what_means_emoji, find_emoji


___ test_what_means_emoji_found(
    what_means_emoji('🐶').lower() __ 'dog face'
    what_means_emoji('🏋').lower() __ 'weight lifter'
    what_means_emoji('🌇').lower() __ 'sunset over buildings'


___ test_what_means_emoji_not_found(
    assert what_means_emoji('aaa').lower() __ 'not found'


___ test_find_matches(capfd
    find_emoji('sun')
    output = capfd.readouterr()[0].lower()
    # some of the results you should get back
    assert 'sunrise' __ output
    assert '🌅' __ output
    assert 'sunset over buildings' __ output
    assert '🌇' __ output
    assert 'sun with face' __ output
    assert '🌻' __ output


___ test_find_no_match(capfd
    find_emoji('awesome')
    output = capfd.readouterr()[0].lower()
    assert not output.strip() or 'no matches' __ output.lower()