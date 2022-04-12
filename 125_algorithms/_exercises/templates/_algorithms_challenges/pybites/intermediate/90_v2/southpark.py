____ c.. _______ C.., d..
____ io _______ StringIO
_______ p.... __ pd
_______ c__

_______ r__

CSV_URL 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


___ get_season_csv_file(season
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    w__ r__.S.. __ s:
        download s.g.. CSV_URL.f..(season
        r.. download.content.d.. 'utf-8')


___ get_num_words_spoken_by_character_per_episode(content
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    

    counts d..(C..)
    

    ___ line __ c__.D.. StringIO(content:
        counts[line 'Character']][line 'Episode']] += l..(line 'Line' .s..

    r.. counts


__ _______ __ _______

    season 1
    get_num_words_spoken_by_character_per_episode(get_season_csv_file(season




