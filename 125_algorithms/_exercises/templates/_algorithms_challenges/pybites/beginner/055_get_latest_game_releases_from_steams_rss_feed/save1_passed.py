from collections import namedtuple
import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')

___ get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    file = feedparser.parse(FEED_URL)
    count = 0
    game_list = []
    for x in file.entries:
        __ count < len(file.entries):
            game_list.append(Game(x.title, x.link))
            count += 1
    return game_list