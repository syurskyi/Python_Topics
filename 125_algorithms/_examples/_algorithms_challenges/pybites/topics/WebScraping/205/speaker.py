from urllib.request import urlretrieve
import os
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")

def get_first_name(fullname):
    name_list = []
    name_list = fullname.split(' ')
    return name_list[0]

def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()
    speakers = soup.find_all('span', class_='speaker')
    speakers_list = []
    for slot_speaker in speakers:
        if ',' in slot_speaker.text.strip():
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

def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    total_speakers = len(first_names)
    female = 0
    d = gender.Detector()
    for name in first_names:
        if d.get_gender(name) in ("female", "mostly_female"):
            female += 1
    return round((female/total_speakers)*100, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    print(names)
    perc = get_percentage_of_female_speakers(names)
    print(perc)







#d = gender.Detector()
#print(d.get_gender(u'Marcos'))