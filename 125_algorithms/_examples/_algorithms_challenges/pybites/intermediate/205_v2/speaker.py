from u__.r.. import u..
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    u..(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """

    speakers = soup.find_all('span',class_='speaker')
    
    first_names = []

    for speaker in speakers:
        text = speaker.getText(strip=True)
        result = re.split(r'\s*,|/\s*',text)
        first_names.extend(r.split()[0] for r in result)

    return first_names








def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    
    d = gender.Detector(case_sensitive=False)
    labels = ('mostly_female','female')
    female_count = 0
    for first_name in first_names:
        result = d.get_gender(first_name)

        female_count += (result in labels)

    return round(female_counts/len(first_names),2)







if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
