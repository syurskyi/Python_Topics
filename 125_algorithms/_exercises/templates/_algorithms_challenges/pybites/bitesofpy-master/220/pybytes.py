from collections ______ namedtuple, Counter
______ re
from datetime ______ datetime
from time ______ strptime, strftime
from typing ______ NamedTuple

______ feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    ___ __init__(self, url=URL
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(URL).entries

    ___ get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        ___ i in self.entries:
            __ domain in i.summary_detail.value:
                yield i.itunes_episode

    ___ get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        dom_count = Counter()
        ___ i in self.entries:
            domains = set(re.findall(r'https?://[^/]+', i.summary_detail.value)) - IGNORE_DOMAINS
            dom_count.update(domains)
        r_ dom_count.most_common(n)

    ___ number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        r_ su.(1 ___ i in self.entries __ SPECIAL_GUEST in i.summary_detail.value)

    ___ _time_to_secs(self, tm: str) -> int:
        parts = [int(s) ___ s in tm.split(':')]
        r_ (parts[0] * 60 + parts[1]) * 60 + parts[2]

    ___ _secs_to_time(self, sec: int) -> str:
        t, s = divmod(sec, 60)
        h, m = divmod(t, 60)
        r_ f'{h:02}:{m:02}:{s:02}'

    ___ get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        # res = Duration('', self.entries[0].itunes_duration, self.entries.entries[0].itunes_duration)
        min_t = max_t = self._time_to_secs(self.entries[0].itunes_duration)
        total_t = min_t
        ___ i in self.entries[1:]:
            _t = self._time_to_secs(i.itunes_duration)
            total_t += _t
            __ _t < min_t:
                min_t = _t
            ____ _t > max_t:
                max_t = _t
        r_ Duration(total_t // le.(self.entries),
                        self._secs_to_time(max_t),
                        self._secs_to_time(min_t))
