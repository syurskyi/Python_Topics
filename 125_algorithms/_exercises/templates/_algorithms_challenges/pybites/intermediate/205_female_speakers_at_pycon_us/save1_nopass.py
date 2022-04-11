____ u__.r.. _______ u..
____ p.. _______ P..

_______ gender_guesser.detector __ gender
____ bs4 _______ BeautifulSoup __ Soup

TMP P..('/tmp')
PYCON_HTML TMP / "pycon2019.html"
PYCON_PAGE ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

__ n.. PYCON_HTML.exists
    u..(PYCON_PAGE, PYCON_HTML)


___ _get_soup(html=PYCON_HTML
    r.. Soup(html.read_text(encoding="utf-8"), "html.parser")


___ get_pycon_speaker_first_names(soup_ N..
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    p..


___ get_percentage_of_female_speakers(first_names
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    p..


__ _____ __ _____
    names get_pycon_speaker_first_names()
    perc get_percentage_of_female_speakers(names)
    print(perc)