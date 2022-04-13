____ c.. _______ C.., d..
_______ c__
____ t___ _______ DefaultDict

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
   header content.s..("\n" 0.s..(",")

   csv_reader c__.D.. [row.s..("\n") ___ row __ content.s..("\n")[1:]], fieldnames=header)

   words_per_episode DefaultDict(C..)
   ___ row __ csv_reader:
      episode_words {row["Episode"]: l..([word ___ word __ row["Line"].s..(" ") __ word !_ ""])}
      words_per_episode[row["Character"]].update(episode_words)

   r.. words_per_episode


__ _______ __ _______
   sp_content get_season_csv_file(1)
   get_num_words_spoken_by_character_per_episode(sp_content)