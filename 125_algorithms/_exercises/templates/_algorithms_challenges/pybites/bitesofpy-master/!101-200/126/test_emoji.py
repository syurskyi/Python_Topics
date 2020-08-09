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
    assert 'sunrise' in output
    assert '🌅' in output
    assert 'sunset over buildings' in output
    assert '🌇' in output
    assert 'sun with face' in output
    assert '🌻' in output


___ test_find_no_match(capfd
    find_emoji('awesome')
    output = capfd.readouterr()[0].lower()
    assert not output.strip() or 'no matches' in output.lower()