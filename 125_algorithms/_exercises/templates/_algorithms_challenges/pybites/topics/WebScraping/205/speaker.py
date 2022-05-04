____ u__.r.. _______ u..
_______ __
____ p.. _______ P..

_______ g__.d.. __ g..
____ ___ _______ B.. __ S..

TMP P.. __.g.. "TMP", "/tmp"
PYCON_HTML ? / "pycon2019.html"
PYCON_PAGE ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

__ n.. P__.e..
    u.. ? ?


___ _get_soup html_?
    r.. S.. ?.r.. e.._ utf-8 "html.parser"

___ get_first_name(fullname
    name_list    # list
    name_list fullname.s..(' ')
    r.. name_list[0]

___ get_pycon_speaker_first_names soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup ?
    speakers ?.f.. 'span', c.._'speaker')
    speakers_list    # list
    ___ slot_speaker __ speakers:
        __ ',' __ slot_speaker.?.s..
            slot_speakers slot_speaker.text.s...s..(',')
            ___ speaker __ slot_speakers:
                speakers_list.a..(get_first_name(speaker.s..()))
        ____ '/' __ slot_speaker.?.s..
            slot_speakers slot_speaker.text.s...s..('/')
            ___ speaker __ slot_speakers:
                speakers_list.a..(get_first_name(speaker.s..()))
        ____
            speakers_list.a..(get_first_name(slot_speaker.?.s..()))
    r.. speakers_list

___ get_percentage_of_female_speakers first_names
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    total_speakers l.. ?
    female 0
    d g__.D..
    ___ name __ fi..
        __ d.get_gender(name) __ ("female", "mostly_female"
            female += 1
    r.. r..((female/total_speakers)*100, 2)


__ _____ __ _____
    names ?
    print(names)
    perc ? ?
    print ?







#d = gender.Detector()
#print(d.get_gender(u'Marcos'))