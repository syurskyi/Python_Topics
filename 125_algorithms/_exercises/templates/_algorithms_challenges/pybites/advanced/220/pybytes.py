____ c.. _______ n.., C..
_______ __
____ t___ _______ N..

_______ f..

SPECIAL_GUEST 'Special guest'

# using _ as min/max are builtins
Duration n..('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


c_ PythonBytes:

    ___ - , url=URL
        """Load the feed url into self.entries using the feedparser module."""
        entries feedparser.p..(URL) 'entries'


    ___ get_episode_numbers_for_mentioned_domain  domain: s..) __ l..:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """

        episode_ids    # list


        ___ entry __ ?
            #summary = entry['summary']
            summary entry 'summary'
            __ domain __ summary:
                episode entry 'itunes_episode'
                episode_ids.a..(episode)


        r.. episode_ids









    ___ get_most_mentioned_domain_names  n: i.. 15) __ l..:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        counts C..()
        ___ entry __ ?
            summary entry 'summary'
            domains s..(__.f.. _ https?://[^/]+',summary
            ___ domain __ domains:
                __ domain n.. __ IGNORE_DOMAINS:
                    counts[domain] += 1

        

        r.. ?.m..(n)


    ___ number_episodes_with_special_guest(self) __ i..
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """

        r.. s..(SPECIAL_GUEST __ entry 'summary'  ___ entry __ entries)

    ___ get_average_duration_episode_in_seconds(self) __ N..:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """


        min_duration_seconds f__('inf')
        max_duration_seconds f__("-inf")
        min_duration max_duration N..
        duration_sums 0


        ___ entry __ ?
            duration= entry 'itunes_duration'
            hours,minutes,seconds m.. i..,duration.s..(':'
            total_seconds 3600 * hours + 60 * minutes + seconds
            duration_sums += total_seconds
            __ total_seconds < min_duration_seconds:
                min_duration_seconds total_seconds
                min_duration duration
            __ total_seconds > max_duration_seconds:
                max_duration_seconds total_seconds
                max_duration duration

        average_duration i..(duration_sums/ l..(entries
        r.. Duration(average_duration,max_duration,min_duration)





__ _______ __ _______


    python_bites PythonBytes()
    python_bites.get_episode_numbers_for_mentioned_domain()

