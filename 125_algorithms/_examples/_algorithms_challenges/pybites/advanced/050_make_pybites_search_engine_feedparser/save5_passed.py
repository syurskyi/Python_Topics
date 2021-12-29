from datetime import datetime
from collections import namedtuple
from time import mktime
from feedparser import parse
import re

# FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


class AttrDict(dict):
    """feedparser lets you access dict keys as attributes, hence a bit of
       mocking, got this from https://stackoverflow.com/a/14620633.
       PyBites uses this class for parsing"""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


dt1 = datetime(2018, 2, 18, 19, 52, 0).timetuple()
dt2 = datetime(2017, 1, 6, 11, 0, 0).timetuple()

FEED = AttrDict({'entries':
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


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    if type(stime) == str:
        format = '%a, %d %b %Y %H:%M:%S %z'
        dt_object = datetime.strptime(stime, format)
        return dt_object.date()
    else:
        return datetime.fromtimestamp(mktime(stime)).date()


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    if type(feed) == AttrDict:
        file = feed
    else:
        file = parse(feed)
    output = []
    for entry in file.entries:
        date = _convert_struct_time_to_dt(entry.published)
        tag_list = [tag['term'].lower() for tag in entry.tags]
        output.append(Entry(date, entry.title, entry.link, tag_list))
    return output


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    search = search.lower()
    tag_list = [tag for tag in entry.tags]
    if not re.search(r'\|', search) and not re.search(r'\&', search):
        return search in tag_list
    if re.search(r'\|', search):
        search = re.split(r'\|', search)
        return any([item in tag_list for item in search])
    if re.search(r'\&', search):
        search = re.split(r'\&', search)
        return all([item in tag_list for item in search])
    return search


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()
    while True:
        try:
            search_term = input('Search for (q for exit): ').lower()
        except EOFError:
            break

        if search_term == '':
            print('Please provide a search term')

        if search_term != '' and search_term != 'q':
            output_list = []
            for entry in entries:
                if filter_entries_by_tag(search_term, entry):
                    output_list.append(entry)
            output_list = sorted(output_list, key=lambda x: x.date)

            titles = [entry.title for entry in output_list]

            output_number = len(output_list)
            if output_number < 1:
                print(f'{output_number} entries matched')
            if output_number == 1:
                for title in titles:
                    print(title)
                print(f'{output_number} entry matched')
            if output_number > 1:
                for title in titles:
                    print(title)
                print(f'{output_number} entries matched')

        if search_term == 'q':
            print('Bye')
            break


if __name__ == '__main__':
    main()


main()
