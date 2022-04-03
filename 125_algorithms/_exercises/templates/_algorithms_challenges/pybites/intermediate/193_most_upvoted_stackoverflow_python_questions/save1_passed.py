_______ r__
____ bs4 _______ BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


___ top_python_questions(url=cached_so_url
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    response = r__.g.. url)
    soup = BeautifulSoup(response.text, 'html.parser')
    right_table = soup.find_all('div', {'class': 'question-summary'})

    q    # list
    vo    # list
    vi    # list
    ___ line __ right_table:
        question = line.find('a', {'class': 'question-hyperlink'}).text
        vote = line.find('span', {'class': 'vote-count-post high-scored-post'})
        view = line.find('div', {'class': 'views supernova'})

        __ vote __ N..
            vote = 0
        ____:
            vote = vote.text

        __ view __ N..
            view = 0
        ____:
            view = view.text.s...s.. [0]

        q.a..(question)
        vo.a..(vote)
        vi.a..(view)

    vi_true    # list
    ___ number __ vi:
        number = s..(number)
        __ number.endswith('k'
            vi_true.a..(f__(number[:-1]) * 1000)
        __ number.endswith('m'
            vi_true.a..(f__(number[:-1]) * 1_000_000)
        __ number __ '0':
            vi_true.a..(f__(number))

    final = l..(z..(q, vo, vi_true))
    output1    # list
    output2    # list
    ___ question, vote, view __ final:
        __ view >= 1_000_000:
            output1.a..(question)
            output2.a..(i..(vote))

    r.. s..(l..(z..(output1, output2)), key=l.... x :x[1], r.._T..