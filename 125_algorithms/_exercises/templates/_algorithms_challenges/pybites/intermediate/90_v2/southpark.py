____ c.. _______ Counter, defaultdict
____ io _______ StringIO
_______ pandas __ pd
_______ csv

_______ requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


___ get_season_csv_file(season
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    w__ requests.Session() __ s:
        download = s.get(CSV_URL.f..(season))
        r.. download.content.d.. 'utf-8')


___ get_num_words_spoken_by_character_per_episode(content
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    

    counts = defaultdict(Counter)
    

    ___ line __ csv.DictReader(StringIO(content)):
        counts[line 'Character']][line 'Episode']] += l..(line 'Line' .s..

    r.. counts


__ _______ __ _______

    season = 1
    get_num_words_spoken_by_character_per_episode(get_season_csv_file(season))




