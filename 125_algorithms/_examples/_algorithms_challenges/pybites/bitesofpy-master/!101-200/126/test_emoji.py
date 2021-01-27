from emoji import what_means_emoji, find_emoji


def test_what_means_emoji_found():
    what_means_emoji('🐶').lower() == 'dog face'
    what_means_emoji('🏋').lower() == 'weight lifter'
    what_means_emoji('🌇').lower() == 'sunset over buildings'


def test_what_means_emoji_not_found():
    a__ what_means_emoji('aaa').lower() == 'not found'


def test_find_matches(capfd):
    find_emoji('sun')
    output = capfd.readouterr()[0].lower()
    # some of the results you should get back
    a__ 'sunrise' in output
    a__ '🌅' in output
    a__ 'sunset over buildings' in output
    a__ '🌇' in output
    a__ 'sun with face' in output
    a__ '🌻' in output


def test_find_no_match(capfd):
    find_emoji('awesome')
    output = capfd.readouterr()[0].lower()
    a__ not output.strip() or 'no matches' in output.lower()