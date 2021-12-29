____ collections _______ Counter, defaultdict
_______ csv
____ typing _______ DefaultDict

_______ requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


___ get_season_csv_file(season):
   """Receives a season int, and downloads loads in its
      corresponding CSV_URL"""
   with requests.Session() as s:
      download = s.get(CSV_URL.format(season))
      r.. download.content.decode('utf-8')


___ get_num_words_spoken_by_character_per_episode(content):
   """Receives loaded csv content (str) and returns a dict of
      keys=characters and values=Counter object,
      which is a mapping of episode=>words spoken"""
   header = content.split("\n")[0].split(",")

   csv_reader = csv.DictReader([row.strip("\n") ___ row __ content.split("\n")[1:]], fieldnames=header)

   words_per_episode = DefaultDict(Counter)
   ___ row __ csv_reader:
      episode_words = {row["Episode"]: l..([word ___ word __ row["Line"].split(" ") __ word != ""])}
      words_per_episode[row["Character"]].update(episode_words)

   r.. words_per_episode


__ __name__ __ "__main__":
   sp_content = get_season_csv_file(1)
   get_num_words_spoken_by_character_per_episode(sp_content)