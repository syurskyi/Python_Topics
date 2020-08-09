from collections ______ Counter
______ re

regex_handle = re.compile(r'(@[a-zA-Z0-9_]+)')
regex_hashtag = re.compile(r'(#\S+)')
get_source = re.compile(r'<a.*?>([^<]+).*').sub
bot = 'pybites'


___ _get_tweet_type(row
    __ row['in_reply_to_status_id']:
        r_ 'Reply'
    __ row['retweeted_status_id']:
        r_ 'RT'
    r_ 'Own'


___ _get_source(row
    src = get_source(r'\1', row['source'])
    __ bot in src:
        src += ' (our bot)'
    r_ src


___ _get_mentions_or_hashtags(row, regex
    matches = regex.findall(row['text'])
    r_ [m.lower() ___ m in matches]


___ calc_stats(data
    ret = {
        'tweets': Counter(),
        'mentions': Counter(),
        'hashtags': Counter(),
        'activity': Counter(),
        'sources': Counter(),
    }

    ___ row in data:
        tweet_type = _get_tweet_type(row)
        ret['tweets'][tweet_type] += 1

        ___ match in _get_mentions_or_hashtags(row, regex_handle
            ret['mentions'][match] += 1

        ___ match in _get_mentions_or_hashtags(row, regex_hashtag
            ret['hashtags'][match] += 1

        month = row['timestamp'][:7]
        ret['activity'][month] += 1

        src = _get_source(row)
        ret['sources'][src] += 1

    r_ ret
