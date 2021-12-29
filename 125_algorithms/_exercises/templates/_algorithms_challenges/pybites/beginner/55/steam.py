from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


___ get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed = feedparser.parse(FEED_URL)

    games = [] 
    for entry in feed['entries']:
        title = entry['title']
        link = entry['link']
        game = Game(title,link)
        games.append(game)


    return games





__ __name__ == "__main__":
    get_games()


