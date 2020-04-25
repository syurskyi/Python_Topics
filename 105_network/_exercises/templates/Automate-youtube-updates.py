____ bs4 ______ BeautifulSoup
______ requests
______ json
____ collections ______ deque


channels _ ['FIFATV', 'bbcnews', 'PewDiePie']
w__ o..('file.json', _) __ file:
    l__t_videos _ json.load(file)

___ channel __ channels:
    r _ requests.get(f'https://www.youtube.com/user/{channel}/videos')
    soup _ BeautifulSoup(r.text, 'lxml')
    matchs _ soup.find_all('a', cl__s__"yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2")
    d _ deque(l__t_videos[channel], 10)
    j _ -1
    ___ i __ ra.. min(le.(d), le.(matchs))
        __ matchs[i]['href'].sp..('=')[1] !_ d[0]:
            j +_ 1
        ____
            b..
    ___ match __ reversed(matchs[:j+1]
        d.appendleft(match["href"].sp..("=")[1])
        print(match.text, '  |  ',
        f'https://www.youtube.com/watch?v={match["href"].sp..("=")[1]}')
    l__t_videos[channel] _ list(d)
    print('______________________________________________________________________________________________')
w__ o..('file.json', 'w') __ file:
    json.dump(l__t_videos, file, indent_2)
