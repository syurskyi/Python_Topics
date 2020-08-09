#!python3
# steam_scraper.py is a simple web scraper to check for the latest steam games

from collections ______ namedtuple
______ sqlite3

______ feedparser

FEED_FILE = "newreleases.xml"
Game = namedtuple('Game', 'Link')
games_list = []

___ check_create_db(
	with sqlite3.connect("steam_games.db") as connection:
		c = connection.cursor()
		try:
			c.execute("""CREATE TABLE new_steam_games
					(N
					ame TEXT, Link TEXT)
					""")		
		except:  
			pass

___ db_connection(
	with sqlite3.connect("steam_games.db") as connection:
		c = connection.cursor()
	r_ c
			
___ main(
	
	check_create_db()
	feed = feedparser.parse(FEED_FILE)
	___ entry in feed['entries']:
		Game = (entry['title'], entry['link'])
		games_list.append(Game)
	
		c = db_connection()
		c.executemany("INSERT INTO new_steam_games VALUES(?, ?)", games_list)
	

__ __name__ __ "__main__":
	main()
