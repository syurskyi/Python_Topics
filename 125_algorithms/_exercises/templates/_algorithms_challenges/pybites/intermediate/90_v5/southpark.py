_______ csv
____ collections _______ Counter, defaultdict
____ io _______ StringIO
_______ requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


___ get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.f..(season))
        r.. download.content.decode('utf-8')


___ get_num_words_spoken_by_character_per_episode(content: s..):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    lines = defaultdict(l.... : Counter())
    ___ row __ [{'episode': x['Episode'], 'character': x['Character'],
                 'words': l..(x['Line'].s..())} ___ x __ csv.DictReader(StringIO(content))]:
        lines[row['character']] += Counter({row['episode']: row['words']})
    r.. lines
