from collections ______ namedtuple
from datetime ______ date

______ feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


___ _convert_struct_time_to_dt(stime
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    r_ date(year=stime.tm_year, month=stime.tm_mon, day=stime.tm_mday)


___ get_feed_entries(feed=FEED
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    f = feedparser.parse(feed)
    result = []
    for item in f.entries:
        result.append(Entry(_convert_struct_time_to_dt(item.published_parsed),
                            item.title,
                            item.link,
                            [t.term.lower() for t in item.tags]))
    r_ result


___ filter_entries_by_tag(search, entry
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
    __ '&' in search:
        r_ all(tag.lower() in entry.tags for tag in search.split('&'))
    __ '|' in search:
        r_ any(tag.lower() in entry.tags for tag in search.split('|'))
    r_ search.lower() in entry.tags


___ main(
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
    w___ True:
        term = input('Search for (q for exit ')
        __ term __ '':
            print('Please provide a search term')
            continue
        __ term __ 'q':
            print('Bye')
            break
        matches = sorted([entry for entry in entries __ filter_entries_by_tag(term, entry)])
        for match in matches:
            print(f'{match.date:10} | {match.title:50} | {match.link}')
        print(f'\n{le.(matches)} entr{"y" __ le.(matches) __ 1 else "ies"} matched')


__ __name__ __ '__main__':
    main()
