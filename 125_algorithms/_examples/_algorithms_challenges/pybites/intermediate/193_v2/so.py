import requests
from bs4 import BeautifulSoup
import re

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as err:
        print('HTTP Error')
        print(err)
    except Exception as err:
        print('Other Error')
        print(err)
    else:
        soup = BeautifulSoup(response.text,'html.parser')


        questions = soup.find_all("div",class_='question-summary')
        results = []
        for question in questions:
            question_text = question.find('a',class_='question-hyperlink').getText()
            views = question.find('div',class_='views').getText()
            if views.strip().split()[0][-1] == 'm':
                votes = int(question.find('span',class_='vote-count-post').strong.getText())
                results.append((question_text,votes))

        
        return sorted(results,key=lambda x: x[1],reverse=True)





if __name__ == "__main__":

    print(top_python_questions())





