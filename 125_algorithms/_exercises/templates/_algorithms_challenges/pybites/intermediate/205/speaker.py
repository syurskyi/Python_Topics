from codecs import ignore_errors
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


___ get_pycon_speaker_first_names(soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    __ soup is None:
        soup = _get_soup()
    
    first_names = []
    soup_speakers = soup.find_all("span", class_="speaker")
    for speaker in soup_speakers:
        speaker_clean = speaker.get_text().strip()
        __ speaker_clean.find(",") > 0:
            for speaker in speaker_clean.split(","):
                first_name = speaker.strip().split(" ")[0].strip()
                first_names.append(first_name)
        elif speaker_clean.find("/") > 0:
            for speaker in speaker_clean.split("/"):
                first_name = speaker.strip().split(" ")[0].strip()
                first_names.append(first_name)        
        else:
            first_names.append(speaker_clean.split(" ")[0])
    return first_names


___ get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    female_counter = 0
    gender_guess = gender.Detector()
    for name in first_names:
        predicted_gender = gender_guess.get_gender(name)
        __ predicted_gender in ["female", "mostly_female"]:
            female_counter += 1

    return round((female_counter/len(first_names)*100), 2)

__ __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)