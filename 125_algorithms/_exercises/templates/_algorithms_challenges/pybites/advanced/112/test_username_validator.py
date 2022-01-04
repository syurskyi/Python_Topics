____ typing.__ _______ Pattern

_______ p__

____ username_validator _______ (Validator,
                                parse_social_platforms_string,
                                validate_username)


___ test_parse_social_platforms_string
    platforms = parse_social_platforms_string()
    ... l..(platforms) __ 3
    ... a..([t..(nw) __ Validator ___ nw __ platforms.v..)
    twitter = platforms.get('Twitter')
    ... t..(twitter.r..) __ r..  # range upper limit = exclusive!
    ... isi..(twitter.regex, Pattern)  # nope, no regex here ;)


___ test_validate_username_wrong_validator
    w__ p__.r..(ValueError):
        validate_username('Github', 'bob')


___ test_validate_username_twitter_range
    ... validate_username('Twitter', 'a')
    ... n.. validate_username('Twitter', '')
    ... n.. validate_username('Twitter', 'a'*16)


___ test_validate_username_twitter_regex
    ... validate_username('Twitter', 'bob')
    ... validate_username('Twitter', 'boB123')
    ... validate_username('Twitter', 'bo__89A')
    ... n.. validate_username('Twitter', 'bob-123')
    ... n.. validate_username('Twitter', 'bob@PyBites')
    ... n.. validate_username('Twitter', 'bob.')


___ test_validate_username_facebook_range
    ... validate_username('Facebook', 'abc123')
    ... n.. validate_username('Facebook', 'bob')
    ... n.. validate_username('Facebook', 'a'*51)


___ test_validate_username_facebook_regex
    ... validate_username('Facebook', 'bobb.')
    ... validate_username('Facebook', 'bob.PyBites')
    ... validate_username('Facebook', 'aAbB123')
    ... n.. validate_username('Facebook', 'bobb,')
    ... n.. validate_username('Facebook', 'bob$56')
    ... n.. validate_username('Facebook', 'bob123_')


___ test_validate_username_reddit_range
    ... validate_username('Reddit', 'abc')
    ... n.. validate_username('Reddit', 'ab')
    ... n.. validate_username('Reddit', 'a'*21)


___ test_validate_username_reddit_regex
    ... validate_username('Reddit', 'bob_PyBites')
    ... validate_username('Reddit', '-123ABC')
    ... validate_username('Reddit', '123-abc__')
    ... n.. validate_username('Reddit', 'bobb.')
    ... n.. validate_username('Reddit', 'bob@PyBites')
    ... n.. validate_username('Reddit', 'bob$56')