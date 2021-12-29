import requests
from bs4 import BeautifulSoup as Soup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'

def load_page(so_url):
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(so_url).content.decode('utf-8')

def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    faq = []
    content = load_page(cached_so_url)
    soup = Soup(content, 'html.parser')
    question_list = [question for question in soup.find_all('div', class_='question-summary')]
    for question in question_list:
        question_text = question.a.text.strip()
        question_vote = question.find('span', class_='vote-count-post').strong.text.strip()
        question_view = question.find('div', class_='views').text.strip()
        if 'm views' in question_view:   
            faq.append((question_text,int(question_vote)))
    return sorted(faq, key=lambda x:x[1], reverse=True)




#print(top_python_questions())