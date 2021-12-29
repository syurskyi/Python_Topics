from collections import Counter, defaultdict
import csv
from typing import DefaultDict

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
   """Receives a season int, and downloads loads in its
      corresponding CSV_URL"""
   with requests.Session() as s:
      download = s.get(CSV_URL.format(season))
      return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
   """Receives loaded csv content (str) and returns a dict of
      keys=characters and values=Counter object,
      which is a mapping of episode=>words spoken"""
   header = content.split("\n")[0].split(",")

   csv_reader = csv.DictReader([row.strip("\n") for row in content.split("\n")[1:]], fieldnames=header)

   words_per_episode = DefaultDict(Counter)
   for row in csv_reader:
      episode_words = {row["Episode"]: len([word for word in row["Line"].split(" ") if word != ""])}
      words_per_episode[row["Character"]].update(episode_words)

   return words_per_episode


if __name__ == "__main__":
   sp_content = get_season_csv_file(1)
   get_num_words_spoken_by_character_per_episode(sp_content)