import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    right_table = soup.find_all('div', {'class': 'question-summary'})

    q = []
    vo = []
    vi = []
    for line in right_table:
        question = line.find('a', {'class': 'question-hyperlink'}).text
        vote = line.find('span', {'class': 'vote-count-post high-scored-post'})
        view = line.find('div', {'class': 'views supernova'})

        if vote is None:
            vote = 0
        else:
            vote = vote.text

        if view is None:
            view = 0
        else:
            view = view.text.strip().split()[0]

        q.append(question)
        vo.append(vote)
        vi.append(view)

    vi_true = []
    for number in vi:
        number = str(number)
        if number.endswith('k'):
            vi_true.append(float(number[:-1]) * 1000)
        if number.endswith('m'):
            vi_true.append(float(number[:-1]) * 1_000_000)
        if number == '0':
            vi_true.append(float(number))

    final = list(zip(q, vo, vi_true))
    output1 = []
    output2 = []
    for question, vote, view in final:
        if view >= 1_000_000:
            output1.append(question)
            output2.append(int(vote))

    return sorted(list(zip(output1, output2)), key=lambda x :x[1], reverse=True)