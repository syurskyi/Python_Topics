____ codecs _______ ignore_errors
____ urllib.request _______ urlretrieve
_______ os
____ pathlib _______ Path

_______ gender_guesser.detector __ gender
____ bs4 _______ BeautifulSoup __ Soup

TMP = Path(os.getenv("TMP", "/tmp"))
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
    
    first_names    # list
    soup_speakers = soup.find_all("span", class_="speaker")
    ___ speaker __ soup_speakers:
        speaker_clean = speaker.get_text().s..
        __ speaker_clean.find(",") > 0:
            ___ speaker __ speaker_clean.s..(","):
                first_name = speaker.s...s..(" ")[0].s..
                first_names.a..(first_name)
        ____ speaker_clean.find("/") > 0:
            ___ speaker __ speaker_clean.s..("/"):
                first_name = speaker.s...s..(" ")[0].s..
                first_names.a..(first_name)
        ____:
            first_names.a..(speaker_clean.s..(" ")[0])
    r.. first_names


___ get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    female_counter = 0
    gender_guess = gender.Detector()
    ___ name __ first_names:
        predicted_gender = gender_guess.get_gender(name)
        __ predicted_gender __ ["female", "mostly_female"]:
            female_counter += 1

    r.. round((female_counter/l..(first_names)*100), 2)

__ __name__ __ '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)