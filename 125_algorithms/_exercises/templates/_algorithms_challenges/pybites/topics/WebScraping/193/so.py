_______ requests
____ bs4 _______ BeautifulSoup __ Soup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'

___ load_page(so_url
    """Download the blog html and return its decoded content"""
    w__ requests.Session() __ session:
        r.. session.get(so_url).content.d.. 'utf-8')

___ top_python_questions(url=cached_so_url
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    faq    # list
    content = load_page(cached_so_url)
    soup = Soup(content, 'html.parser')
    question_list = [question ___ question __ soup.find_all('div', class_='question-summary')]
    ___ question __ question_list:
        question_text = question.a.text.s..
        question_vote = question.find('span', class_='vote-count-post').strong.text.s..
        question_view = question.find('div', class_='views').text.s..
        __ 'm views' __ question_view:
            faq.a..((question_text,i..(question_vote)))
    r.. s..(faq, key=l.... x:x[1], r.._T..




#print(top_python_questions())