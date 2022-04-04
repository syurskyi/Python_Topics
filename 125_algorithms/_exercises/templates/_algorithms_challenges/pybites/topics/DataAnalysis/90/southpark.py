____ c.. _______ C.., d..
_______ csv

_______ r__

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


___ get_season_csv_file(season
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    w__ r__.S.. __ s:
        download = s.g.. CSV_URL.f..(season))
        r.. download.content.d.. 'utf-8')


___ get_num_words_spoken_by_character_per_episode(content
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    spoken_word = d..(C..)
    lines = csv.DictReader(content.s..
    ___ line __ lines:
        spoken_word[line 'Character']][line 'Episode']] += l..(line 'Line' .s..
    r.. spoken_word

print(get_num_words_spoken_by_character_per_episode(get_season_csv_file(1)))