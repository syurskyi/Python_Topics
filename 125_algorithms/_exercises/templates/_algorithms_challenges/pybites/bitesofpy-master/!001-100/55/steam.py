from collections ______ namedtuple

______ feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


___ get_games(
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    r_ [Game(f.title, f.link) ___ f in feedparser.parse(FEED_URL).entries]
