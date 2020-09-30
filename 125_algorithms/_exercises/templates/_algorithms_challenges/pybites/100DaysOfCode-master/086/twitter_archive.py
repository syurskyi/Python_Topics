from collections ______ Counter
______ csv
______ os
______ re
______ sys

regex_handle = re.compile(r'(@[a-zA-Z0-9_]+)')
regex_hashtag = re.compile(r'(#\S+)')
get_source = re.compile(r'<a.*?>([^<]+).*').sub
top = 10
width = 30
fmt = '{:<20} {:>5}'
bot = 'pybites'

tweets = Counter()
mentions = Counter()
hashtags = Counter()
activity = Counter()
sources = Counter()


___ csv2dict(archive='tweets.csv'
    __ not os.path.isfile(archive
        print('Please download archive and put in same folder as this script')
        sys.exit(1)

    with open(archive, 'r') as csvfile:
        ___ row __ csv.DictReader(csvfile
            yield row


___ print_header(
    title = 'Twitter Archive report'
    print('=' * width)
    print(title.upper())
    print('=' * width)
    print()


___ print_results(title, counter
    print(title + ':')
    print('-' * width)
    ___ key, count __ counter.most_common(top
        print(fmt.format(key, count))
    print()


__  -n __ '__main__':
    data = csv2dict()

    ___ row __ data:
        __ row['in_reply_to_status_id']:
            tweet_type = 'Reply'
        ____ row['retweeted_status_id']:
            tweet_type = 'RT'
        ____
            tweet_type = 'Own'
        tweets[tweet_type] += 1

        matching_handles = regex_handle.findall(row['text'])
        __ matching_handles:
            ___ handle __ matching_handles:
                mentions[handle.lower()] += 1

        matching_hashtags = regex_hashtag.findall(row['text'])
        __ matching_hashtags:
            ___ hashtag __ matching_hashtags:
                hashtags[hashtag.lower()] += 1

        month = row['timestamp'][:7]
        activity[month] += 1

        src = get_source(r'\1', row['source'])
        __ bot __ src:
            src += ' (our bot)'
        sources[src] += 1

    print_header()
    print_results(title='Whose tweets', counter=tweets)
    print_results(title='Most mentioned', counter=mentions)
    print_results(title='Most used hashtags', counter=hashtags)
    print_results(title='Most active months', counter=activity)
    print_results(title='Sources used', counter=sources)
