____ c.. _______ n..

_______ feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = n..('Game', 'title link')


___ get_games
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed = feedparser.p..(FEED_URL)
    r.. [ Game(entry.get('title'), entry.get('link')) ___ entry __ feed 'entries'  ]

#get_games()
#print(len(get_games()))