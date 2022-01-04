____ steam _______ get_games

# should mock this out but let's call feedparser for real
# for a feedparser mocking see the AttrDict (advanced) Bite 50's tests
games = get_games()


___ test_assert_number_of_entries
    ... l..(games) __ 30


___ test_all_list_items_are_namedtuples
    ... a..(isi..(game, tuple) ___ game __ games)


___ test_assert_all_links_contain_store
    ... a..('store.steampowered.com' __ game.link ___ game __ games)


___ test_title_and_url_first_entry
    first_game = games[0]
    ... first_game.title __ 'Midweek Madness - RiME, 33% Off'
    ... first_game.link __ 'http://store.steampowered.com/news/31695/'


___ test_title_and_url_last_entry
    last_game = games[-1]
    ... last_game.title __ 'Now Available on Steam - Loco Dojo, 35% off!'
    ... last_game.link __ 'http://store.steampowered.com/news/31113/'