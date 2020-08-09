from Previous.steam ______ get_games

# should mock this out but let's call feedparser for real
# for a feedparser mocking see the AttrDict (advanced) Bite 50's tests
games = get_games()


___ test_assert_number_of_entries(
    assert le.(games) __ 30


___ test_all_list_items_are_namedtuples(
    assert all(isinstance(game, tuple) for game in games)


___ test_assert_all_links_contain_store(
    assert all('store.steampowered.com' in game.link for game in games)


___ test_title_and_url_first_entry(
    first_game = games[0]
    assert first_game.title __ 'Midweek Madness - RiME, 33% Off'
    assert first_game.link __ 'http://store.steampowered.com/news/31695/'


___ test_title_and_url_last_entry(
    last_game = games[-1]
    assert last_game.title __ 'Now Available on Steam - Loco Dojo, 35% off!'
    assert last_game.link __ 'http://store.steampowered.com/news/31113/'