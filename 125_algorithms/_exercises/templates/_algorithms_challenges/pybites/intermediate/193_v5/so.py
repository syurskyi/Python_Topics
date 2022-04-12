_______ r__
____ bs4 _______ BeautifulSoup

cached_so_url 'https://bit.ly/2IMrXdp'


___ load_page(url
    """Download the blog html and return its decoded content"""
    w__ r__.S.. __ session:
        r.. session.g.. url).content.d.. 'utf-8')


___ top_python_questions(url=cached_so_url
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    content load_page(url)
    soup BeautifulSoup(content)
    questions [(question.select_one('a.question-hyperlink').s__.s..,
                  i..(question.select_one('span.vote-count-post').s__.s..()))
                 ___ question __ soup.find_all(class_='question-summary')
                 __ question.select_one('div.views').s__.s...e.. 'm views')]
    r.. s..(questions, k.._l.... x: -x[1])
