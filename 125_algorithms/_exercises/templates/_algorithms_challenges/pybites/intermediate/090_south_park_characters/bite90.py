____ c.. _______ C.., d..
_______ c__
_______ r__

CSV_URL 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501

___ get_season_csv_file(season=1
   "Receives a season int, and downloads loads in its corresponding CSV_URL"
   w__ r__.S.. __ s:
      download s.g.. CSV_URL.f..(season
      r.. download.content.d.. 'utf-8')


___ get_num_words_spoken_by_character_per_episode(content=get_season_csv_file:
   """
   Receives loaded csv content (str) and returns a dict of keys=characters and values=Counter object,
   which is a mapping of episode=>words spoken
   """
   data c__.D.. content.s.. , delimiter=',')
   character_words_per_episode d..(C..)
   ___ record __ data:
      character_words_per_episode[record 'Character']][record  'Episode']] += l..(record 'Line' .s..
   r.. character_words_per_episode
