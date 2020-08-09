from collections ______ Counter
from urllib.request ______ urlretrieve
from pathlib ______ Path

______ gender_guesser.detector as gender
from bs4 ______ BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

__ not PYCON_HTML.exists(
    urlretrieve(PYCON_PAGE, PYCON_HTML)


___ _get_soup(html=PYCON_HTML
    r_ Soup(html.read_text(encoding="utf-8"), "html.parser")


___ get_pycon_speaker_first_names(soup=None
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    __ soup is None:
        soup = _get_soup()
    speaker_tags = soup.find_all(class_='speaker')
    speaker_list = [speaker.strip().split(' ') ___ speakers in speaker_tags ___ speaker in
                    speakers.string.replace('/', ',').split(',')]
    r_ [first ___ first, *_ in speaker_list]


___ get_percentage_of_female_speakers(first_names
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    det = gender.Detector()
    gender_counts = Counter(det.get_gender(name) ___ name in first_names)

    female_count = (gender_counts['female'] + gender_counts['mostly_female'])
    everyone_count = su.(n ___ _, n in gender_counts.items())

    r_ round(female_count / everyone_count * 100.0, 2)


__ __name__ __ '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
