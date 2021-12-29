_______ requests
____ bs4 _______ BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


___ load_page(url):
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        r.. session.get(url).content.decode('utf-8')


___ top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    content = load_page(url)
    soup = BeautifulSoup(content)
    questions = [(question.select_one('a.question-hyperlink').string.strip(),
                  int(question.select_one('span.vote-count-post').string.strip()))
                 ___ question __ soup.find_all(class_='question-summary')
                 __ question.select_one('div.views').string.strip().endswith('m views')]
    r.. s..(questions, key=l.... x: -x[1])
