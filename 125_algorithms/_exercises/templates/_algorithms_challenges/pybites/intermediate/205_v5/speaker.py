____ c.. _______ Counter
____ urllib.request _______ urlretrieve
____ pathlib _______ Path

_______ gender_guesser.detector __ gender
____ bs4 _______ BeautifulSoup __ Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

__ n.. PYCON_HTML.exists
    urlretrieve(PYCON_PAGE, PYCON_HTML)


___ _get_soup(html=PYCON_HTML):
    r.. Soup(html.read_text(encoding="utf-8"), "html.parser")


___ get_pycon_speaker_first_names(soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    __ soup __ N..
        soup = _get_soup()
    speaker_tags = soup.find_all(class_='speaker')
    speaker_list = [speaker.s...s..(' ') ___ speakers __ speaker_tags ___ speaker __
                    speakers.s__.r..('/', ',').s..(',')]
    r.. [first ___ first, *_ __ speaker_list]


___ get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    det = gender.Detector()
    gender_counts = Counter(det.get_gender(name) ___ name __ first_names)

    female_count = (gender_counts['female'] + gender_counts['mostly_female'])
    everyone_count = s..(n ___ _, n __ gender_counts.i..

    r.. r..(female_count / everyone_count * 100.0, 2)


__ _____ __ _____
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
