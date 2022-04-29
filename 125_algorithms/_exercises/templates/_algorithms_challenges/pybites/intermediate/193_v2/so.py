_______ r__
____ ___ _______ B..
_______ __

cached_so_url 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


___ top_python_questions url_?
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """

    ___
        response r__.g.. url)
        response.raise_for_status()
    ______ r__.HTTPError __ err:
        print('HTTP Error')
        print(err)
    ______ E.. __ err:
        print('Other Error')
        print(err)
    ____
        soup B..(?.t..,'html.parser')


        questions ?.f.. "div",c.._'question-summary')
        results    # list
        ___ question __ questions:
            question_text question.f.. 'a',c.._'question-hyperlink').g.. )
            views question.f.. 'div',c.._'views').g.. )
            __ views.s...s.. [0][-1] __ 'm':
                votes i..(question.f.. 'span',c.._'vote-count-post').strong.getText
                results.a..((question_text,votes

        
        r.. s..(results,k.._l.... x: ? 1r.._T..





__ _______ __ _______

    print(top_python_questions





