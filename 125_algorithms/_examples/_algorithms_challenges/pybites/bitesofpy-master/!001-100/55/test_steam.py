from Previous.steam import get_games

# should mock this out but let's call feedparser for real
# for a feedparser mocking see the AttrDict (advanced) Bite 50's tests
games = get_games()


def test_assert_number_of_entries():
    a__ len(games) == 30


def test_all_list_items_are_namedtuples():
    a__ all(isinstance(game, tuple) for game in games)


def test_assert_all_links_contain_store():
    a__ all('store.steampowered.com' in game.link for game in games)


def test_title_and_url_first_entry():
    first_game = games[0]
    a__ first_game.title == 'Midweek Madness - RiME, 33% Off'
    a__ first_game.link == 'http://store.steampowered.com/news/31695/'


def test_title_and_url_last_entry():
    last_game = games[-1]
    a__ last_game.title == 'Now Available on Steam - Loco Dojo, 35% off!'
    a__ last_game.link == 'http://store.steampowered.com/news/31113/'