from urllib.request import urlretrieve
import os
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

__ not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


___ _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")

___ get_first_name(fullname):
    name_list = []
    name_list = fullname.split(' ')
    return name_list[0]

___ get_pycon_speaker_first_names(soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()
    speakers = soup.find_all('span', class_='speaker')
    speakers_list = []
    for slot_speaker in speakers:
        __ ',' in slot_speaker.text.strip():
            slot_speakers = slot_speaker.text.strip().split(',')
            for speaker in slot_speakers:
                speakers_list.append(get_first_name(speaker.strip()))
        elif '/' in slot_speaker.text.strip():
            slot_speakers = slot_speaker.text.strip().split('/')
            for speaker in slot_speakers:
                speakers_list.append(get_first_name(speaker.strip()))
        else:
            speakers_list.append(get_first_name(slot_speaker.text.strip()))
    return speakers_list

___ get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    total_speakers = len(first_names)
    female = 0
    d = gender.Detector()
    for name in first_names:
        __ d.get_gender(name) in ("female", "mostly_female"):
            female += 1
    return round((female/total_speakers)*100, 2)


__ __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    print(names)
    perc = get_percentage_of_female_speakers(names)
    print(perc)







#d = gender.Detector()
#print(d.get_gender(u'Marcos'))