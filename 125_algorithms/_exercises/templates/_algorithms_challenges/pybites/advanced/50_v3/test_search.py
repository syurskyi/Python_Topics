____ d__ _______ d__, date
____ unittest.mock _______ patch

_______ p__

____ s.. _______ (_convert_struct_time_to_dt, get_feed_entries,
                    filter_entries_by_tag, main, Entry)


c_ AttrDict(d..):
    """feedparser lets you access dict keys as attributes, hence a bit of
       mocking, got this from https://stackoverflow.com/a/14620633"""
    ___ - , *args, **kwargs):
        super(AttrDict, self).__init__ $ $$
        __dict__ = self


dt1 = d__(2018, 2, 18, 19, 52, 0).timetuple()
dt2 = d__(2017, 1, 6, 11, 0, 0).timetuple()

MOCK_ENTRIES = AttrDict({'entries':
                [AttrDict({'author': 'PyBites',
                           'link':
                           'https://pybit.es/twitter_digest_201808.html',  # noqa E501
                           'published': 'Sun, 18 Feb 2018 20:52:00 +0100',  # noqa E501
                           'published_parsed': dt1,
                           'summary': 'Every weekend we share ...',
                           'tags': [AttrDict({'term': 'twitter'}),
                                    AttrDict({'term': 'Flask'}),
                                    AttrDict({'term': 'Python'}),
                                    AttrDict({'term': 'Regex'})],
                           'title': 'Twitter Digest 2018 Week 08'}),
                 AttrDict({'author': 'Julian',
                           'link': 'https://pybit.es/pyperclip.html',
                           'published': 'Fri, 06 Jan 2017 12:00:00 +0100',  # noqa E501
                           'published_parsed': dt2,
                           'summary': 'Use the Pyperclip module to ...',
                           'tags': [AttrDict({'term': 'python'}),
                                    AttrDict({'term': 'tips'}),
                                    AttrDict({'term': 'tricks'}),
                                    AttrDict({'term': 'code'}),
                                    AttrDict({'term': 'pybites'})],
                           'title': 'Copy and Paste with Pyperclip'})]})


?p__.m__.p.("arg, ret", [
    (d__(2017, 9, 12, 8, 50, 0).timetuple(),
     date y.._2017,  m.._9,  d.._12)),
    (d__(2017, 9, 8, 14, 30, 0).timetuple(),
     date y.._2017,  m.._9,  d.._8)),
    (d__(2016, 12, 19, 9, 26, 0).timetuple(),
     date y.._2016,  m.._12,  d.._19)),
])
___ test_convert_struct_time_to_dt(arg, ret):
    ... _convert_struct_time_to_dt(arg) __ ret


@patch("feedparser.parse", side_effect=[MOCK_ENTRIES])
___ test_get_feed_entries(inp):
    first, last = t..(get_feed_entries())

    ... first.date __ date y.._2018,  m.._2,  d.._18)
    ... first.title __ 'Twitter Digest 2018 Week 08'
    ... first.link __ 'https://pybit.es/twitter_digest_201808.html'
    expected = ['flask', 'python', 'regex', 'twitter']
    # allow list or set
    ... s..(l..(first.tags)) __ expected

    ... last.date __ date y.._2017,  m.._1,  d.._6)
    ... last.title __ 'Copy and Paste with Pyperclip'
    ... last.link __ 'https://pybit.es/pyperclip.html'
    expected = ['code', 'pybites', 'python', 'tips', 'tricks']
    ... s..(l..(last.tags)) __ expected


?p__.m__.p.("arg, ret", [
    ('blabla', F..),
    ('tricks', T..),
    ('TRICKS', T..),  # case should not matter
    ('TriCkS', T..),
    ('python', F..),  # whole term only so python != pythonic
    ('matplotlib&pandas', T..),
    ('matplotlib&pandas&collections', T..),
    ('matplotlib&pandas&flask', F..),
    ('matplotlib|flask', T..),
    ('matplotlib|django|flask', T..),
    ('pyramid|django|flask', F..),
])
___ test_filter_entries_by_tag(arg, ret):
    entry = Entry(date=date(2016, 12, 22),
                  title='2016 py articles and useful books',
                  link='https://pybit.es/py-articles-books2016.html',
                  tags={'pythonic', 'data science',
                        'tips', 'tricks', 'matplotlib',
                        'pandas', 'books', 'collections'})
    ... filter_entries_by_tag(arg, entry) __ ret


@patch("feedparser.parse", side_effect=[MOCK_ENTRIES])
@patch("builtins.input", side_effect=['pycon', 'twitter', 'python', 'nonsense',
                                      'python|regex', 'python&regex', 'REGeX',
                                      '', 'q'])
___ test_main(entries, inp, capfd):
    main()
    out, _ = capfd.readouterr()

    output = [line ___ line __ out.s..('\n') __ line.s..]
    expected = ['0 entries matched', 'Twitter Digest 2018 Week 08',
                '1 entry matched', 'Copy and Paste with Pyperclip',
                'Twitter Digest 2018 Week 08', '2 entries matched',
                '0 entries matched', 'Copy and Paste with Pyperclip',
                'Twitter Digest 2018 Week 08', '2 entries matched',
                'Twitter Digest 2018 Week 08', '1 entry matched',
                'Twitter Digest 2018 Week 08', '1 entry matched',
                'Please provide a search term', 'Bye']
    ___ line, exp __ z..(output, expected):
        ... exp __ line