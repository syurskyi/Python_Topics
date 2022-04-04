____ u__.r.. _______ u..
____ p.. _______ P..

_______ gender_guesser.detector __ gender
____ bs4 _______ BeautifulSoup __ Soup

TMP = P..('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
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

    speakers = soup.find_all('span',class_='speaker')
    
    first_names    # list

    ___ speaker __ speakers:
        text = speaker.getText(s..=T..)
        result = __.s..(r'\s*,|/\s*',text)
        first_names.extend(r.s.. [0] ___ r __ result)

    r.. first_names








___ get_percentage_of_female_speakers(first_names
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    
    d = gender.Detector(case_sensitive=F..)
    labels = ('mostly_female','female')
    female_count = 0
    ___ first_name __ first_names:
        result = d.get_gender(first_name)

        female_count += (result __ labels)

    r.. r..(female_counts/l..(first_names),2)







__ _____ __ _____
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
