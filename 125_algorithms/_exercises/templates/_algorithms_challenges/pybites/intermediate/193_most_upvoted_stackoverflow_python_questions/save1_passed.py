_______ r__
____ ___ _______ B..

cached_so_url 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


___ top_python_questions(url=cached_so_url
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    response r__.g.. url)
    soup B..(?.t.., 'html.parser')
    right_table ?.f.. 'div', {'class': 'question-summary'})

    q    # list
    vo    # list
    vi    # list
    ___ line __ right_table:
        question line.f.. 'a', {'class': 'question-hyperlink'}).text
        vote line.f.. 'span', {'class': 'vote-count-post high-scored-post'})
        view line.f.. 'div', {'class': 'views supernova'})

        __ vote __ N..
            vote 0
        ____
            vote vote.text

        __ view __ N..
            view 0
        ____
            view view.text.s...s.. [0]

        q.a..(question)
        vo.a..(vote)
        vi.a..(view)

    vi_true    # list
    ___ number __ vi:
        number s.. ?
        __ number.e.. 'k'
            vi_true.a..(f__(number[:-1]) * 1000)
        __ number.e.. 'm'
            vi_true.a..(f__(number[:-1]) * 1_000_000)
        __ number __ '0':
            vi_true.a..(f__(number

    final l..(z..(q, vo, vi_true
    output1    # list
    output2    # list
    ___ question, vote, view __ final:
        __ view >_ 1_000_000:
            output1.a..(question)
            output2.a..(i..(vote

    r.. s..(l..(z..(output1, output2, k.._l.... x :x[1], r.._T..