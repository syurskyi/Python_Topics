____ c.. _______ C.., d..
_______ csv
_______ __
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

    words_spoken = d..(C..)
    rows = csv.reader(content.s..
    next(rows)                  # skip header
    ___ row __ rows:
        epi, char, line = row[1:]
        num_words = l..(__.f..(r'(\S+)', line))
        words_spoken[char].update({epi: num_words})

    r.. words_spoken
