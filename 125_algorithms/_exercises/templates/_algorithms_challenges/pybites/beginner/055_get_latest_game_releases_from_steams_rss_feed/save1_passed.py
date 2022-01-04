____ collections _______ n..
_______ feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = n..('Game', 'title link')

___ get_games
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    file = feedparser.parse(FEED_URL)
    count = 0
    game_list    # list
    ___ x __ file.entries:
        __ count < l..(file.entries):
            game_list.a..(Game(x.title, x.link))
            count += 1
    r.. game_list