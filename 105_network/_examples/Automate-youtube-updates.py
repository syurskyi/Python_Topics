from bs4 import BeautifulSoup
import requests
import json
from collections import deque


channels = ['FIFATV', 'bbcnews', 'PewDiePie']
with open('file.json', 'r') as file:
    last_videos = json.load(file)

for channel in channels:
    r = requests.get(f'https://www.youtube.com/user/{channel}/videos')
    soup = BeautifulSoup(r.text, 'lxml')
    matchs = soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2")
    d = deque(last_videos[channel], 10)
    j = -1
    for i in range(min(len(d), len(matchs))):
        if matchs[i]['href'].split('=')[1] != d[0]:
            j += 1
        else:
            break
    for match in reversed(matchs[:j+1]):
        d.appendleft(match["href"].split("=")[1])
        print(match.text, '  |  ',
        f'https://www.youtube.com/watch?v={match["href"].split("=")[1]}')
    last_videos[channel] = list(d)
    print('______________________________________________________________________________________________')
with open('file.json', 'w') as file:
    json.dump(last_videos, file, indent=2)
