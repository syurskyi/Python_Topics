import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup
import requests
import re

PYCON_HTML = 'https://bites-data.s3.us-east-2.amazonaws.com/pycon2019.html'

___ _get_soup(html=PYCON_HTML):
    response = requests.get(PYCON_HTML)
    return Soup(response.content, "html.parser")


___ get_pycon_speaker_first_names(soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()

    speakers = []
    for speaker in soup.find_all('span', 'speaker'):
        speaker = speaker.text.strip()

        # Multiple speakers separated by comma
        __ re.match(r'.*,.*', speaker):
            multiple_speakers = speaker.split(', ')
            for s in multiple_speakers:
                speakers.append(s.split()[0])

        # Multiple speakers seperated by slash
        elif re.match(r'.*/.*', speaker):
            multiple_speakers = speaker.split(' / ')
            for s in multiple_speakers:
                speakers.append(s.split()[0])

        # Speaker name begins with acronym
        elif re.match(r'[A-Z]\.', speaker):
            speakers.append(speaker.split()[1])

        else:
            speakers.append(speaker.split()[0])

    return speakers


___ get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    d = gender.Detector(case_sensitive=False)
    genders = [d.get_gender(speaker) for speaker in first_names]
    total_speakers = len(genders)
    female_speakers = len([g for g in genders __ g is 'female' or g is 'mostly_female'])
    return round(female_speakers / total_speakers * 100, 2)


__ __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)