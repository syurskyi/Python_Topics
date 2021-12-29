from collections import namedtuple
from datetime import date
import datetime
from time import mktime

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """

    dt = datetime.datetime.fromtimestamp(mktime(stime))

    return dt.date()



def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    d = feedparser.parse(feed)
    entries = d.entries
    
    all_entries =[]
    for entry in entries:
        title = entry.title
        link = entry.link
        date = entry.published_parsed
        tags = entry.tags
        tags = [t.get('term').lower() for t in tags]

        date = _convert_struct_time_to_dt(date)


        entry = Entry(date,title,link,tags)
        all_entries.append(entry)

    return all_entries






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
        
    entry_tags = entry.tags
    if '&' in search:
        splits = search.split('&')

        return all(split.lower() in entry_tags for split in splits)
    elif '|' in search:
        splits = search.split('|')
        return any(split.lower() in entry_tags for split in splits)
    else:
        return search.lower() in entry_tags

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
    
    entries.sort(key=lambda x: x.date)
    while True:
        term = input("Search Term? ")
        if term == '':
            print('Please provide a search term')
            continue
        if term == 'q':
            print('Bye')
            break
        
        
        matches = 0
        for entry in entries:
            found = filter_entries_by_tag(term,entry)
            if found:
                print(entry.title)
                matches += 1

        
        if matches == 1:
            print('1 entry matched')
        else:
            print(f"{matches} entries matched")



if __name__ == '__main__':
    main()
