_______ r__
____ ___ _______ B.. __ S..

cached_so_url 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'

___ load_page(so_url
    """Download the blog html and return its decoded content"""
    w__ r__.S.. __ session
        r.. ?.g.. so_url).c__.d.. utf-8

___ top_python_questions url_?
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    faq    # list
    content load_page(cached_so_url)
    soup S.. ? html.parser
    question_list [question ___ question __ ?.f.. 'div', c.._'question-summary')]
    ___ question __ question_list:
        question_text question.a.?.s..
        question_vote question.f.. 'span', c.._'vote-count-post').strong.?.s..
        question_view question.f.. 'div', c.._'views').?.s..
        __ 'm views' __ question_view:
            faq.a..((question_text,i..(question_vote)))
    r.. s..(faq, k.._l.... x:x[1], r.._T..




#print(top_python_questions())