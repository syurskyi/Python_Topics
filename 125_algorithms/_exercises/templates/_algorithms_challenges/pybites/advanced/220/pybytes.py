from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    ___ __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(URL)['entries']


    ___ get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """

        episode_ids = []


        for entry in self.entries:
            #summary = entry['summary']
            summary = entry['summary']
            __ domain in summary:
                episode = entry['itunes_episode']
                episode_ids.append(episode)


        return episode_ids









    ___ get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        counts = Counter()
        for entry in self.entries:
            summary = entry['summary']
            domains = set(re.findall(r'https?://[^/]+',summary))
            for domain in domains:
                __ domain not in IGNORE_DOMAINS:
                    counts[domain] += 1

        

        return counts.most_common(n)


    ___ number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """

        return sum(SPECIAL_GUEST in entry['summary'] for entry in self.entries)

    ___ get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """


        min_duration_seconds = float('inf')
        max_duration_seconds = float("-inf")
        min_duration = max_duration = None
        duration_sums = 0


        for entry in self.entries:
            duration= entry['itunes_duration']
            hours,minutes,seconds = map(int,duration.split(':'))
            total_seconds = 3600 * hours + 60 * minutes + seconds
            duration_sums += total_seconds
            __ total_seconds < min_duration_seconds:
                min_duration_seconds = total_seconds
                min_duration = duration
            __ total_seconds > max_duration_seconds:
                max_duration_seconds = total_seconds
                max_duration = duration

        average_duration = int(duration_sums/ len(self.entries))
        return Duration(average_duration,max_duration,min_duration)





__ __name__ == "__main__":


    python_bites = PythonBytes()
    python_bites.get_episode_numbers_for_mentioned_domain()

