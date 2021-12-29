____ collections _______ Counter, defaultdict
_______ csv
_______ requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501

___ get_season_csv_file(season=1):
   "Receives a season int, and downloads loads in its corresponding CSV_URL"
   with requests.Session() as s:
      download = s.get(CSV_URL.f..(season))
      r.. download.content.decode('utf-8')


___ get_num_words_spoken_by_character_per_episode(content=get_season_csv_file()):
   """
   Receives loaded csv content (str) and returns a dict of keys=characters and values=Counter object,
   which is a mapping of episode=>words spoken
   """
   data = csv.DictReader(content.splitlines(), delimiter=',')
   character_words_per_episode = defaultdict(Counter)
   ___ record __ data:
      character_words_per_episode[record['Character']][record ['Episode']] += l..(record['Line'].s..())
   r.. character_words_per_episode
