____ states _______ (get_every_nth_state, get_state_abbrev,
                    get_longest_state, combine_state_names_and_abbreviations,
                    states, us_state_abbrev, NOT_FOUND)


___ test_get_every_nth_state():
    expected = ['Massachusetts', 'Missouri', 'Hawaii',
                'Vermont', 'Delaware']
    ... l..(get_every_nth_state()) __ expected
    expected = ['Missouri', 'Vermont']
    ... l..(get_every_nth_state(n=20)) __ expected


___ test_get_state_abbrev():
    ... get_state_abbrev('Illinois') __ 'IL'
    ... get_state_abbrev('North Dakota') __ 'ND'
    ... get_state_abbrev('bogus') __ NOT_FOUND


___ test_get_longest_state():
    # depending the direction of the sort (reversed or not)
    # both North and South Carolina are correct
    possible_answers = ('North Carolina', 'South Carolina')
    ... get_longest_state(us_state_abbrev) __ possible_answers
    ... get_longest_state(states) __ possible_answers


___ test_combine_state_names_and_abbreviations():
    expected = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'South Dakota', 'Tennessee', 'Texas', 'Utah',
                'Vermont', 'Virginia', 'Washington', 'West Virginia',
                'Wisconsin', 'Wyoming']
    ... combine_state_names_and_abbreviations() __ expected