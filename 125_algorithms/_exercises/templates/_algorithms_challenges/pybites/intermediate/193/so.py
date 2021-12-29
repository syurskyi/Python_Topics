import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


___ top_python_questions(url=cached_so_url):
   """Use requests to retrieve the url / html,
      parse the questions out of the html with BeautifulSoup,
      filter them by >= 1m views ("..m views").
      Return a list of (question, num_votes) tuples ordered
      by num_votes descending (see tests for expected output).
   """
   response = requests.get(url)
   soup = BeautifulSoup(response.text, "html.parser")
   ge_1m = []
   lt_1m = []

   question_summary = soup.find_all("div", class_="question-summary")
   for question in question_summary:
      views = int(question.find("div", class_="views").get("title").split(" ")[0].replace(",", ""))
      _question = question.find("a", class_="question-hyperlink").get_text()
      votes = int(question.find("span", class_="vote-count-post").get_text())
      
      __ views >= 1000000:
         ge_1m.append((_question, votes))
      else:
         lt_1m.append((_question, votes))

   return sorted(ge_1m, key=lambda x: x[1], reverse=True)


__ __name__ == "__main__":
   print(top_python_questions())