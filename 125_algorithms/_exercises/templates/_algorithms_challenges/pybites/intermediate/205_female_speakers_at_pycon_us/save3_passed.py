_______ gender_guesser.detector __ gender
____ bs4 _______ BeautifulSoup __ Soup
_______ requests
_______ __

PYCON_HTML = 'https://bites-data.s3.us-east-2.amazonaws.com/pycon2019.html'

___ _get_soup(html=PYCON_HTML):
    response = requests.get(PYCON_HTML)
    r.. Soup(response.content, "html.parser")


___ get_pycon_speaker_first_names(soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()

    speakers    # list
    ___ speaker __ soup.find_all('span', 'speaker'):
        speaker = speaker.text.s..

        # Multiple speakers separated by comma
        __ __.m..(r'.*,.*', speaker):
            multiple_speakers = speaker.s..(', ')
            ___ s __ multiple_speakers:
                speakers.a..(s.s.. [0])

        # Multiple speakers seperated by slash
        ____ __.m..(r'.*/.*', speaker):
            multiple_speakers = speaker.s..(' / ')
            ___ s __ multiple_speakers:
                speakers.a..(s.s.. [0])

        # Speaker name begins with acronym
        ____ __.m..(r'[A-Z]\.', speaker):
            speakers.a..(speaker.s.. [1])

        ____:
            speakers.a..(speaker.s.. [0])

    r.. speakers


___ get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    d = gender.Detector(case_sensitive=F..)
    genders = [d.get_gender(speaker) ___ speaker __ first_names]
    total_speakers = l..(genders)
    female_speakers = l..([g ___ g __ genders __ g __ 'female' o. g __ 'mostly_female'])
    r.. round(female_speakers / total_speakers * 100, 2)


__ __name__ __ '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)