_______ c__
____ c.. _______ C.., d..
____ io _______ StringIO
_______ r__

CSV_URL 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


___ get_season_csv_file(season
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    w__ r__.S.. __ s:
        download s.g.. CSV_URL.f..(season
        r.. download.content.d.. 'utf-8')


___ get_num_words_spoken_by_character_per_episode(content: s..
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    lines d..(l.... : C..
    ___ row __ [{'episode': x 'Episode' , 'character': x 'Character' ,
                 'words': l..(x 'Line' .s..} ___ x __ c__.DictReader(StringIO(content]:
        lines[row 'character']] += C..({row 'episode' : row 'words' })
    r.. lines
